from PIL import Image
import os

def convert_image(source_path):
    """
    Converts images to webp if they are in png, jpg, jpeg, bmp, or gif format.
    Converts webp images to high-quality png.
    The converted image is saved in the same location as the original picture.
    """
    source_path = source_path.strip()
    file_name, file_extension = os.path.splitext(source_path)
    target_path = ""

    png_quality_settings = {"quality": 95}

    if file_extension.lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
        target_path = f"{file_name}.webp"
        target_format = "WEBP"
    elif file_extension.lower() == ".webp":
        target_path = f"{file_name}_hq.png".replace('.webp', '')
        target_format = "PNG"

    with Image.open(source_path) as image:
        if target_format == "PNG":
            image.save(target_path, target_format, **png_quality_settings)
        else:
            image.save(target_path, target_format)
        print(f"Converted '{source_path}' to '{target_path}' successfully.")

if __name__ == "__main__":
    source_path = input("Enter the path to your image: ").strip()
    convert_image(source_path)
