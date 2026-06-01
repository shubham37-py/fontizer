import cv2
import matplotlib.pyplot as plt

def clean_handwriting(image_path):
    # 1. Load the image
    # OpenCV loads images in BGR (Blue, Green, Red) format.
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not load image. Check the path.")
        return

    # 2. Convert to Grayscale
    # Color data is useless for shape detection. Strip it out to save memory.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Gaussian Blur
    # Blurs the image slightly to smooth out paper texture and minor camera noise.
    # The (5, 5) is the kernel size (must be odd numbers).
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 4. Adaptive Thresholding (The Game Changer)
    # Simple thresholding fails with shadows. Adaptive thresholding calculates 
    # the threshold dynamically for small regions, isolating the ink perfectly.
    # We use THRESH_BINARY_INV to make the background black and the text white.
    thresh = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # 5. Visualize the pipeline
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original')

    plt.subplot(1, 3, 2)
    plt.imshow(gray, cmap='gray')
    plt.title('Grayscale + Blur')

    plt.subplot(1, 3, 3)
    plt.imshow(thresh, cmap='gray')
    plt.title('Binary Threshold (Isolated Text)')

    plt.tight_layout()
    plt.show()

# --- Execution ---
# Replace 'test.jpg' with an actual photo of your handwriting on a blank piece of paper.
clean_handwriting('test.jpg')