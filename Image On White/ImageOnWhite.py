import cv2
import numpy as np
import os

def overlay_image_on_white_bg(image_path, output_path):
    # Load the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if img is None:
        print(f"Skipping invalid image: {image_path}")
        return
    
    # Get image dimensions
    img_height, img_width = img.shape[:2]
    
    # Create a white background (1080x1920)
    bg_height, bg_width = 1920, 1080
    white_bg = np.ones((bg_height, bg_width, 3), dtype=np.uint8) * 255
    
    # Resize if image is too large
    if img_height > bg_height or img_width > bg_width:
        scale_factor = min(bg_width / img_width, bg_height / img_height)
        img_width = int(img_width * scale_factor)
        img_height = int(img_height * scale_factor)
        img = cv2.resize(img, (img_width, img_height), interpolation=cv2.INTER_AREA)

    # Recalculate offset after resizing
    x_offset = (bg_width - img_width) // 2
    y_offset = (bg_height - img_height) // 2
    
    # Overlay image onto white background
    white_bg[y_offset:y_offset + img_height, x_offset:x_offset + img_width] = img
    
    # Save the output
    cv2.imwrite(output_path, white_bg)
    print(f"Saved: {output_path}")

def process_all_images(input_folder="input", output_folder="output"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            overlay_image_on_white_bg(input_path, output_path)

# Run the batch processor
process_all_images()
