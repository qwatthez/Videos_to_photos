# FrameExtract — Camera Trap Frame Extractor

*Extract photos from camera trap videos for easier analysis *

## English

### Overview

**FrameExtract** is a specialized tool for extracting individual frames from **camera trap videos** into high-quality images. Camera traps can be used to record continuous video footage, but still images are significantly lighter, easier to manage, and ideal for data sharing. Convert your wildlife monitoring videos into sequences of photos and prepare them for platforms like [Agouti.eu](https://www.agouti.eu).

**Why extract frames from camera trap videos?**
-  **Lighter files** — Individual photos are much smaller than video files, making them easier to store and share
-  **Better analysis** — Focus on specific behavioral moments without video playback
-  **Platform compatibility** — Easily upload extracted images to camera trap monitoring platforms like Agouti.eu
-  **Efficient cataloging** — Rename, tag, and organize individual frames for ecological surveys
-  **Data preservation** — Extract and preserve important sightings from long video sequences

Perfect for:
- Wildlife monitoring and ecological surveys
- Camera trap data processing and management
- Preparing camera trap images for Agouti.eu and similar data platforms

### Features

 **Automatic Frame Extraction** — Extract frames from your camera trap videos (MP4, MOV, AVI)
 **Real-time Progress Tracking** — Monitor extraction progress with live statistics
 **Modern UI** — Beautiful, responsive interface designed for wildlife researchers
 **Bilingual** — Full French/English language support with instant switching
 **Customizable Extraction** — Control extraction interval, start delay, and image size
 **Batch Processing** — Process multiple camera trap videos at once
 **Download as ZIP** — Get all extracted frames in a single ZIP file for easy sharing
 **EXIF Metadata** — Automatically preserves timestamp information in extracted images
 **Wildlife-Ready** — Images prepared for platforms like Agouti.eu

### Quick Start

#### Prerequisites
- Python 3.7+
- pip or conda

#### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Videos_to_photos.git
cd Videos_to_photos
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open in your browser**
Visit `http://localhost:5000`

### Usage

1. **Upload videos** — Drag and drop or browse to select one or multiple video files
2. **Configure settings**:
   - **Interval (s)**: Frequency of frame extraction (e.g., 1 second)
   - **Start delay (s)**: Skip the beginning of the video
   - **Image size**: Resize extracted images (10-100% of original)
3. **Start extraction** — Click the extraction button
4. **Download results** — Get your ZIP file with all extracted images

### Supported Formats

- MP4 (H.264, H.265)
- MOV (QuickTime)
- AVI (MPEG-4, Motion JPEG)

### Configuration

Edit `app.py` to customize:
- Upload folder location
- Output folder location
- Application secret key
- Port and host settings

### Project Structure

```
Videos_to_photos/
├── app.py                 # Flask application & frame extraction logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface with embedded styles & scripts
├── uploads/              # Temporary upload storage
└── outputs/              # Extracted frames storage
```

### Technologies

- **Backend**: Flask (Python)
- **Video Processing**: OpenCV (cv2)
- **Image Processing**: Pillow (PIL)
- **EXIF Handling**: piexif
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **UI Components**: Modern CSS Grid & Flexbox, Responsive Design

### Performance

- **Real-time progress updates** via polling
- **Asynchronous frame extraction** using threading
- **Efficient file handling** with ZIP streaming
- **Optimized image encoding** with quality preservation

### Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers

### Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

### License

This project is licensed under the MIT License.

### Support

For issues or questions, please open an issue on GitHub or contact the project maintainer.

---

## Français

### Présentation

**FrameExtract** est un outil spécialisé pour extraire des images individuelles de **vidéos de pièges photographiques** vers des images de haute qualité. Les pièges photos enregistrent des séquences vidéo continues, mais les images fixes sont beaucoup plus légères, plus faciles à gérer et idéales pour l'analyse comportementale et le partage de données. Extrayez les moments clés de vos vidéos de suivi de la faune et préparez-les pour des plateformes comme [Agouti.eu](https://www.agouti.eu).

**Pourquoi extraire des images de vidéos de pièges photos?**
- 📊 **Fichiers plus légers** — Les photos individuelles sont beaucoup plus petites que les fichiers vidéo, ce qui les rend plus faciles à stocker et à partager
- 🎯 **Meilleure analyse** — Concentrez-vous sur des moments comportementaux spécifiques sans lecture vidéo
- 🌐 **Compatibilité des plateformes** — Téléchargez facilement les images extraites sur des plateformes de suivi de la faune comme Agouti.eu
- ⚡ **Catalogage efficace** — Renommez, étiquetez et organisez les images individuelles pour les relevés écologiques
- 💾 **Préservation des données** — Extrayez et conservez les observations importantes des longues séquences vidéo

Parfait pour :
- Le suivi de la faune et les relevés écologiques
- Le traitement et la gestion des données de pièges photos
- Extraction des moments comportementaux du suivi vidéo continu
- Préparation des images de pièges photos pour Agouti.eu et d'autres plateformes de données

### Fonctionnalités

✨ **Extraction Automatique d'Images** — Extrait les images de vos vidéos de pièges photos (MP4, MOV, AVI)
⚡ **Suivi de Progression en Temps Réel** — Surveillez la progression avec des statistiques en direct
🎨 **Interface Moderne** — Belle interface réactive conçue pour les chercheurs en faune
🌍 **Bilingue** — Support complet du français/anglais avec basculement instantané
⚙️ **Extraction Personnalisable** — Contrôlez l'intervalle d'extraction, le délai au démarrage et la taille des images
📦 **Traitement par Lots** — Traitez plusieurs vidéos de pièges photos à la fois
📥 **Télécharger en ZIP** — Obtenez toutes les images extraites dans un seul fichier ZIP
🖼️ **Métadonnées EXIF** — Préserve automatiquement les informations d'horodatage dans les images extraites
🐾 **Prêt pour Agouti** — Images préparées pour les plateformes comme Agouti.eu

### Démarrage Rapide

#### Prérequis
- Python 3.7+
- pip ou conda

#### Installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/votreusername/Videos_to_photos.git
cd Videos_to_photos
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Lancer l'application**
```bash
python app.py
```

5. **Ouvrir dans le navigateur**
Visitez `http://localhost:5000`

### Utilisation

1. **Uploader les vidéos** — Glissez-déposez ou parcourez pour sélectionner une ou plusieurs vidéos
2. **Configurer les paramètres** :
   - **Intervalle (s)** : Fréquence d'extraction des images (ex. 1 seconde)
   - **Délai départ (s)** : Ignorer le début de la vidéo
   - **Taille des images** : Redimensionner les images extraites (10-100% de l'original)
3. **Lancer l'extraction** — Cliquez sur le bouton d'extraction
4. **Télécharger les résultats** — Obtenez votre fichier ZIP avec toutes les images extraites

### Formats Supportés

- MP4 (H.264, H.265)
- MOV (QuickTime)
- AVI (MPEG-4, Motion JPEG)

### Configuration

Modifiez `app.py` pour personnaliser :
- Localisation du dossier d'upload
- Localisation du dossier de sortie
- Clé secrète de l'application
- Paramètres de port et d'hôte

### Structure du Projet

```
Videos_to_photos/
├── app.py                 # Application Flask et logique d'extraction
├── requirements.txt       # Dépendances Python
├── templates/
│   └── index.html        # Interface Web avec styles et scripts intégrés
├── uploads/              # Stockage temporaire des uploads
└── outputs/              # Stockage des images extraites
```

### Technologies

- **Backend** : Flask (Python)
- **Traitement Vidéo** : OpenCV (cv2)
- **Traitement d'Images** : Pillow (PIL)
- **Gestion EXIF** : piexif
- **Frontend** : JavaScript Vanilla, HTML5, CSS3
- **Composants UI** : CSS Grid & Flexbox Modernes, Design Responsive

### Performance

- **Mises à jour de progression en temps réel** via sondage
- **Extraction d'images asynchrone** utilisant du threading
- **Gestion efficace des fichiers** avec streaming ZIP
- **Codage d'image optimisé** avec préservation de la qualité

### Compatibilité Navigateurs

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Navigateurs mobiles

### Contribution

Les contributions sont bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Suggérer des fonctionnalités
- Soumettre des pull requests

### Licence

Ce projet est sous licence MIT.

### Support

Pour toute question ou problème, veuillez ouvrir une issue sur GitHub ou contacter le responsable du projet.
