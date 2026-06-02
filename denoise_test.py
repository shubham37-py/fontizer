import cv2
import matplotlib.pyplot as plt



# The Power of the Median Filter
# To fix this, we are deploying a Median Blur. Unlike other smoothing filters (like a Gaussian blur, which calculates a weighted average and can make sharp text edges blurry), a Median Blur is an order-statistic filter.

# It works by sliding a window (called a kernel) across every single pixel in the image. It pulls all the pixel values inside that window, sorts them numerically, and replaces the center pixel with the exact median (middle) value. Because your noise spots are tiny white dots entirely surrounded by black background pixels, they fall at the absolute end of the sorted array and get instantly overwritten with pure black. The sharp edges of your ink line remain completely undamaged.

# Below is an interactive simulator designed to show you exactly how a Median Blur works down at the pixel layer. You can see how raw, noisy text transformations clear up as you adjust the sliding filter window size.

def test_denoising(image_path):
    # 1. Load your noisy letter in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load {image_path}")
        return

    # 2. Apply Median Blur
    # The '5' is the kernel size (a 5x5 pixel grid). It must be an odd number.
    # If the dots are really big, you might need to increase this to 7.
    denoised = cv2.medianBlur(img, 5)

    # 3. Visualize Before and After
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original (With Dandruff)')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(denoised, cmap='gray')
    plt.title('After Median Blur (Clean)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# --- Execution ---
# Replace this string with the exact path to your letter 'e'
test_denoising('dataset/char_3.png')