from PIL import Image
import os

def optimize_image(input_path, output_path, max_size=1080, quality=85):
    """
    Optimize and scale down an image.
    """
    with Image.open(input_path) as img:
        img.thumbnail((max_size, max_size))
        img.save(output_path, optimize=True, quality=quality)

def process_folder(input_folder, output_folder, max_size=1080, quality=85):
    """
    Recursively process and optimize all images in the folder and subfolders.
    """
    for root, dirs, files in os.walk(input_folder):
        relative_path = os.path.relpath(root, input_folder)
        current_output_folder = os.path.join(output_folder, relative_path)

        if not os.path.exists(current_output_folder):
            os.makedirs(current_output_folder)

        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(current_output_folder, filename)
                optimize_image(input_path, output_path, max_size, quality)
                print(f"Optimized: {input_path} -> {output_path}")

def main():
    input_folder = input("Enter the path to your image folder: ").strip().strip('"\'')
    output_folder = f"{input_folder}_optimized"

    process_folder(input_folder, output_folder)
    print(f"Optimization complete. Optimized images are saved in: {output_folder}")

if __name__ == "__main__":
    main()

