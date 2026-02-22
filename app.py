from flask import Flask, render_template, request, jsonify, send_file, session
import cv2
import piexif
from PIL import Image
import os
import datetime
import time
import threading
import uuid
import zipfile
import io

app = Flask(__name__)
app.secret_key = 'video_frame_extractor_secret'

# Store job progress in memory
jobs = {}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def get_creation_time(path):
    try:
        epoch = int(os.stat(path).st_birthtime)
    except AttributeError:
        epoch = int(os.stat(path).st_mtime)
    return datetime.datetime.fromtimestamp(epoch)


def resize_image(image, resize_factor):
    new_width = int(image.width * resize_factor)
    new_height = int(image.height * resize_factor)
    return image.resize((new_width, new_height))


def extract_frames_from_video(path, output_folder, interval_s=1, delay_s=0.5, resize=None, job_id=None, file_index=0, total_files=1):
    start = time.time()

    # Try to load exif template if available
    exif_bytes = None
    try:
        exif_template = piexif.load("template_exif.JPG")
        has_exif = True
    except Exception:
        has_exif = False

    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_gap = max(1, int(fps * interval_s))
    delay = int(delay_s * fps)
    index_to_extract = [i for i in range(delay, total_frames, frames_gap)]

    creation_time = get_creation_time(path)
    file_name = os.path.splitext(os.path.basename(path))[0]
    n_frames = len(index_to_extract)

    for i, frame_index in enumerate(index_to_extract):
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = video.read()
        if not ret:
            continue
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if resize:
            image = resize_image(image, resize)

        seconds_since_start = frame_index / fps
        timestamp = creation_time + datetime.timedelta(seconds=seconds_since_start)

        if has_exif:
            exif_template["Exif"][piexif.ExifIFD.DateTimeOriginal] = timestamp.strftime("%Y:%m:%d %H:%M:%S")
            exif_template["Exif"][piexif.ExifIFD.DateTimeDigitized] = timestamp.strftime("%Y:%m:%d %H:%M:%S")
            exif_bytes = piexif.dump(exif_template)

        output_path = os.path.join(output_folder, f"{file_name}_{i:04d}.jpg")
        if exif_bytes:
            image.save(output_path, 'JPEG', exif=exif_bytes)
        else:
            image.save(output_path, 'JPEG', quality=90)

        # Update progress
        if job_id and job_id in jobs:
            file_progress = (i + 1) / n_frames
            overall = (file_index + file_progress) / total_files * 100
            jobs[job_id]['progress'] = round(overall)
            jobs[job_id]['current_file'] = os.path.basename(path)
            jobs[job_id]['frames_done'] = jobs[job_id].get('frames_accumulated', 0) + i + 1
            jobs[job_id]['files_done'] = file_index

    video.release()
    stop = time.time()
    return n_frames, round(stop - start, 2)


def run_extraction(job_id, video_paths, output_folder, interval_s, delay_s, resize):
    try:
        jobs[job_id]['status'] = 'running'
        total = len(video_paths)
        total_frames = 0

        for idx, path in enumerate(video_paths):
            n, t = extract_frames_from_video(
                path, output_folder,
                interval_s=interval_s,
                delay_s=delay_s,
                resize=resize,
                job_id=job_id,
                file_index=idx,
                total_files=total
            )
            total_frames += n
            jobs[job_id]['frames_accumulated'] = total_frames
            jobs[job_id]['files_done'] = idx + 1

        jobs[job_id]['status'] = 'done'
        jobs[job_id]['progress'] = 100
        jobs[job_id]['total_frames'] = total_frames
        jobs[job_id]['output_folder'] = output_folder

    except Exception as e:
        jobs[job_id]['status'] = 'error'
        jobs[job_id]['error'] = str(e)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    files = request.files.getlist('videos')
    if not files or files[0].filename == '':
        return jsonify({'error': 'No files uploaded'}), 400

    interval_s = float(request.form.get('interval_s', 1))
    delay_s = float(request.form.get('delay_s', 0.5))
    resize = request.form.get('resize_factor', None)
    resize = float(resize) if resize and float(resize) < 1.0 else None

    job_id = str(uuid.uuid4())[:8]
    job_output = os.path.join(OUTPUT_FOLDER, job_id)
    os.makedirs(job_output, exist_ok=True)

    saved_paths = []
    for f in files:
        if f.filename.lower().endswith(('.mov', '.mp4', '.avi')):
            dest = os.path.join(UPLOAD_FOLDER, f"{job_id}_{f.filename}")
            f.save(dest)
            saved_paths.append(dest)

    if not saved_paths:
        return jsonify({'error': 'No valid video files (MP4, MOV, AVI)'}), 400

    jobs[job_id] = {
        'status': 'queued',
        'progress': 0,
        'total_files': len(saved_paths),
        'frames_done': 0,
        'current_file': '',
    }

    thread = threading.Thread(target=run_extraction, args=(job_id, saved_paths, job_output, interval_s, delay_s, resize))
    thread.daemon = True
    thread.start()

    return jsonify({'job_id': job_id})


@app.route('/progress/<job_id>')
def progress(job_id):
    if job_id not in jobs:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(jobs[job_id])


@app.route('/download/<job_id>')
def download(job_id):
    if job_id not in jobs or jobs[job_id]['status'] != 'done':
        return jsonify({'error': 'Job not ready'}), 400

    output_folder = jobs[job_id]['output_folder']
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fname in os.listdir(output_folder):
            fpath = os.path.join(output_folder, fname)
            zf.write(fpath, fname)
    zip_buffer.seek(0)
    return send_file(zip_buffer, mimetype='application/zip', as_attachment=True, download_name=f'frames_{job_id}.zip')


if __name__ == '__main__':
    app.run(debug=True)

