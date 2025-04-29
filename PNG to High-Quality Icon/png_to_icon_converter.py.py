import os
from PIL import Image

def make_image_square(img):
    width, height = img.size
    if width == height:
        return img  # already square

    max_side = max(width, height)
    # Create a transparent square canvas
    new_img = Image.new("RGBA", (max_side, max_side), (0, 0, 0, 0))
    # Paste the original image in the center
    new_img.paste(img, ((max_side - width) // 2, (max_side - height) // 2))
    return new_img

def convert_png_to_icon(png_path, icon_path, sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]):
    try:
        img = Image.open(png_path).convert("RGBA")
        img = make_image_square(img)  # make it square with transparent background
        img.save(icon_path, format='ICO', sizes=sizes)
        print(f"Icon saved as {icon_path} with sizes: {sizes}")
        return True
    except Exception as e:
        print(f"Error converting {png_path}: {e}")
        return False

def batch_convert_pngs_to_icons():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    png_folder = os.path.join(script_dir, "PNGs")
    icon_folder = os.path.join(script_dir, "Icons")

    if not os.path.exists(png_folder):
        print(f"Folder 'PNGs' not found at {png_folder}")
        return

    # Create Icons folder if it doesn't exist
    if not os.path.exists(icon_folder):
        os.makedirs(icon_folder)

    for filename in os.listdir(png_folder):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(png_folder, filename)
            icon_filename = os.path.splitext(filename)[0] + '.ico'
            icon_path = os.path.join(icon_folder, icon_filename)
            
            success = convert_png_to_icon(png_path, icon_path)

            if success:
                try:
                    os.remove(png_path)
                    print(f"Deleted PNG: {png_path}")
                except Exception as e:
                    print(f"Error deleting {png_path}: {e}")

if __name__ == "__main__":
    batch_convert_pngs_to_icons()
