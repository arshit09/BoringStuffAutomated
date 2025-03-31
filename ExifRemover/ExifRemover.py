import os
from PIL import Image

def remove_exif_data_from_folder(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image (e.g., .jpg or .jpeg)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(folder_path, filename)
            output_image_path = os.path.join(folder_path, f"no_exif_{filename}")

            # Open the image
            try:
                with Image.open(input_image_path) as img:
                    # Save the image without EXIF data
                    img.save(output_image_path, format=img.format)
                print(f"EXIF data removed from {filename} and saved to {output_image_path}")
            except Exception as e:
                print(f"Could not process {filename}: {e}")

# Example usage
folder_path = r'folder_path' # Replace with the path to the folder containing images
remove_exif_data_from_folder(folder_path)
