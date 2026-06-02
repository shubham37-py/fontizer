import cv2
import svgwrite
import os

def image_to_svg(image_path, output_svg_path):
    # 1. Load the clean image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load {image_path}")
        return

    # 2. Binary threshold
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # 3. Find Contours
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

    height, width = img.shape
    dwg = svgwrite.Drawing(output_svg_path, size=(width, height), profile='tiny')

    # THE FIX: Combine all contours into a SINGLE string
    combined_path_data = ""
    
    if contours:
        for contour in contours:
            if cv2.contourArea(contour) > 10:
                # Add this contour's math to the master string
                combined_path_data += f"M {contour[0][0][0]},{contour[0][0][1]} "
                for i in range(1, len(contour)):
                    combined_path_data += f"L {contour[i][0][0]},{contour[i][0][1]} "
                # The space after Z is critical so the next subpath doesn't break
                combined_path_data += "Z " 
                
    # 4. Draw the SINGLE combined path to the canvas, punching the holes
    if combined_path_data:
        dwg.add(dwg.path(d=combined_path_data, fill='black', fill_rule='evenodd'))

    dwg.save()
    print(f"Bug squashed. Successfully vectorized to {output_svg_path}")

# --- Execution ---
image_to_svg('dataset/char_10.png', 'vector_e.svg')