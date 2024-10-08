from PIL import Image
import os

def convert_to_webp(source_folder):
    # Create the output folder inside the source folder
    output_folder = os.path.join(source_folder, 'webp')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # File path
            file_path = os.path.join(source_folder, filename)
            
            # Open the image
            with Image.open(file_path) as img:
                # Convert to WebP
                output_file_path = os.path.join(output_folder, filename.split('.')[0] + '.webp')
                img.save(output_file_path, 'webp')

    print("Conversion complete.")

# Prompt user for source folder
source_folder = input("Enter the path to the source folder: ")
convert_to_webp(source_folder)
