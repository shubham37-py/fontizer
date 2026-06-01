# Fontizer 🖋️
**From Raw Pixels to Custom Fonts.**

Fontizer is a Python-based Computer Vision application that takes a raw, messy photograph of handwritten text and converts it into a fully functional, installable custom font (`.ttf`). 

Unlike basic OCR (Optical Character Recognition) that simply reads text and outputs standard system fonts, Fontizer isolates the unique geometric paths of an individual's handwriting, translates those raster pixels into vector graphics (Bezier curves), and compiles them into a personalized typography file.

## 🚀 The Motivation
I built this project to dive deep into the messy realities of Computer Vision. Real-world data is chaotic—lighting is uneven, paper has texture, and shadows destroy simple algorithms. This project is a hands-on exploration of advanced image preprocessing, contour segmentation, and raster-to-vector mathematical transformations. 

*Currently building this project in public on LinkedIn. Follow the journey!*

## 🧠 The Pipeline (How it Works)
Fontizer processes images in distinct, heavily engineered phases:

- **Phase 1: Image Preprocessing (Complete)**
  - Strips useless color data (Grayscale conversion).
  - Smooths high-frequency camera noise (Gaussian Blur).
  - Dynamically isolates ink from shadows and paper texture using **Adaptive Thresholding**, resulting in a pure binary image.
- **Phase 2: Character Segmentation (In Progress)**
  - Utilizing OpenCV contour detection to draw bounding boxes around individual letters and isolate them as standalone mathematical matrices.
- **Phase 3: Raster-to-Vector Conversion (Upcoming)**
  - Tracing the outer and inner boundaries of the pixel data to generate scalable vector paths.
- **Phase 4: Font Compilation (Upcoming)**
  - Mapping the vectorized shapes to specific Unicode characters and packaging them into a `.ttf` file.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **Matrix Operations:** NumPy
* **Data Visualization:** Matplotlib
* **Environment:** Virtualenv (Fully isolated dependencies)

## 💻 Running the Preprocessing Pipeline Locally
1. Clone this repository.
2. Activate your virtual environment: `.\.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt` *(Note: We will generate this file soon!)*
4. Drop a photo of handwriting named `test.jpg` into the working directory.
5. Run the pipeline: `python preprocess.py`
