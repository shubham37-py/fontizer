import cv2
import os
import shutil

def extract_and_clean_characters(image_path, output_folder="dataset"):
    # 1. Reset the dataset folder (delete old dirty data, make a fresh folder)
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)

    # 2. Base Preprocessing
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load {image_path}")
        return
        
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
    )

    # 3. THE ARCHITECTURE FIX: Annihilate the noise on the entire canvas
    # We apply the median blur to the whole thresholded image BEFORE we look for contours.
    clean_canvas = cv2.medianBlur(thresh, 5)

    # 4. Find Contours (Now searching on a perfectly clean canvas)
    contours, _ = cv2.findContours(clean_canvas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 5. Filter and Sort
    bounding_boxes = []
    for contour in contours:
        if cv2.contourArea(contour) > 50:
            x, y, w, h = cv2.boundingRect(contour)
            bounding_boxes.append((x, y, w, h))

    # Sort left-to-right, top-to-bottom
    bounding_boxes = sorted(bounding_boxes, key=lambda b: (b[1] // 50, b[0]))

    # 6. Crop and Save (Extracting from the clean_canvas!)
    count = 1
    for (x, y, w, h) in bounding_boxes:
        padding = 10
        y1 = max(0, y - padding)
        y2 = min(img.shape[0], y + h + padding)
        x1 = max(0, x - padding)
        x2 = min(img.shape[1], x + w + padding)

        # Slice from the noise-free binary canvas
        roi = clean_canvas[y1:y2, x1:x2] 
        
        filename = os.path.join(output_folder, f"char_{count}.png")
        cv2.imwrite(filename, roi)
        count += 1

    print(f"Pipeline complete! Extracted {count-1} perfectly clean characters.")

# --- Execution ---
extract_and_clean_characters('test.jpg')