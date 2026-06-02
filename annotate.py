import cv2
import os
import matplotlib.pyplot as plt

def label_dataset(dataset_folder="dataset"):
    # 1. Get all the PNG files in the folder
    files = [f for f in os.listdir(dataset_folder) if f.endswith('.png')]
    
    # Sort them so they appear in the order they were extracted
    files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]) if '_' in x else 0)

    print(f"Found {len(files)} characters to label.\n")
    print("INSTRUCTIONS:")
    print("Look at the popup image, then type the exact character in this terminal.")
    print("For uppercase, type 'A'. For lowercase, type 'a'.")
    print("Close the popup window after you look at it to continue!\n")

    for filename in files:
        filepath = os.path.join(dataset_folder, filename)
        
        # 2. Show the image
        img = cv2.imread(filepath)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title('What letter is this? (Close window to type)')
        plt.axis('off')
        
        # plt.show(block=True) pauses the script until you close the image window
        plt.show(block=True) 

        # 3. Get user input from the terminal
        char_label = input(f"Enter character for {filename}: ")

        # 4. Handle safety (Windows doesn't let you name files with special characters like / \ : * ? " < > |)
        # But letters and numbers are perfectly safe.
        if len(char_label) == 1 and char_label.isalnum():
            # If uppercase, add a tag so Windows doesn't confuse 'a.png' and 'A.png'
            if char_label.isupper():
                new_name = f"{char_label}_upper.png"
            else:
                new_name = f"{char_label}_lower.png"
                
            new_filepath = os.path.join(dataset_folder, new_name)
            
            # Rename the file
            os.rename(filepath, new_filepath)
            print(f"Renamed to {new_name}\n")
        else:
            print(f"Skipping or invalid input. Kept as {filename}\n")

    print("Annotation complete! Check your dataset folder.")

# --- Execution ---
label_dataset()