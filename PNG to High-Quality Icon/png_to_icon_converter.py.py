from PIL import Image

def convert_png_to_icon(png_path, icon_path, sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)]):
    try:
        img = Image.open(png_path)
        img.save(icon_path, format='ICO', sizes=sizes)
        print(f"Icon saved as {icon_path} with sizes: {sizes}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
convert_png_to_icon(r"your_png_file.png", "your_icon.ico")
