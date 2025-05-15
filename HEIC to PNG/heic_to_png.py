import os
from PIL import Image
import pillow_heif

def convert_heic_to_png(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(directory, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(directory, png_filename)

            try:
                heif_file = pillow_heif.read_heif(heic_path)
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data
                )
                image.save(png_path, "PNG")
                print(f"[✓] Converted: {filename} → {png_filename}")
            except Exception as e:
                print(f"[X] Failed to convert {filename}: {e}")

if __name__ == "__main__":
    current_directory = os.path.dirname(os.path.abspath(__file__))
    convert_heic_to_png(current_directory)
    input("\nDone. Press Enter to exit...")
