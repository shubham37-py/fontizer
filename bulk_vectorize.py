import cv2
import svgwrite
import os
import shutil

def bulk_vectorize(input_folder="dataset", output_folder="vectors"):
    # 1. Prepare the output folder (delete old one if it exists to prevent mixing)
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder, exist_ok=True)
    
    # 2. Grab all our beautifully labeled PNGs
    files = [f for f in os.listdir(input_folder) if f.endswith('.png')]
    
    print(f"Starting bulk vectorization for {len(files)} characters...\n")
    
    # 3. The Math Loop
    for filename in files:
        image_path = os.path.join(input_folder, filename)
        
        # Change the extension from .png to .svg for the output name
        svg_filename = filename.replace('.png', '.svg')
        output_svg_path = os.path.join(output_folder, svg_filename)
        
        # Load clean image
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
            
        # Binary threshold (Safety check)
        _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        # Find Contours
        contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
        
        height, width = img.shape
        dwg = svgwrite.Drawing(output_svg_path, size=(width, height), profile='tiny')
        
        combined_path_data = ""
        if contours:
            for contour in contours:
                if cv2.contourArea(contour) > 10:
                    combined_path_data += f"M {contour[0][0][0]},{contour[0][0][1]} "
                    for i in range(1, len(contour)):
                        combined_path_data += f"L {contour[i][0][0]},{contour[i][0][1]} "
                    combined_path_data += "Z " 
                    
        # Draw and punch holes
        if combined_path_data:
            dwg.add(dwg.path(d=combined_path_data, fill='black', fill_rule='evenodd'))
            dwg.save()
            print(f"Vectorized: {filename} -> {svg_filename}")
            
    print(f"\nSuccess! All {len(files)} mathematical SVGs saved to the '{output_folder}' folder.")

# --- Execution ---
bulk_vectorize()