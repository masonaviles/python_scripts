import os
import subprocess
from PIL import Image
from datetime import datetime

def convert_nef_to_tiff(nef_file_path):
    try:
        subprocess.run(['dcraw', '-v', '-w', '-T', nef_file_path], check=True)
        print(f"Converted {nef_file_path} to TIFF successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {nef_file_path} to TIFF. Error: {e}")

def convert_tiff_to_png(tiff_file_path, png_file_path):
    with Image.open(tiff_file_path) as img:
        img.save(png_file_path)
        print(f"Converted {tiff_file_path} to {png_file_path} successfully.")

def process_folder(input_folder_path):
    today = datetime.now()
    output_folder_name = today.strftime("%m-%d-%Y")
    output_folder_path = os.path.join(os.path.dirname(input_folder_path), output_folder_name)

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for filename in os.listdir(input_folder_path):
        if filename.lower().endswith('.nef'):
            print(f"Processing {filename}...")
            base_filename = os.path.splitext(filename)[0]
            nef_file_path = os.path.join(input_folder_path, filename)
            tiff_file_path = os.path.join(input_folder_path, base_filename + '.tiff')
            png_file_path = os.path.join(output_folder_path, base_filename + '.png')

            convert_nef_to_tiff(nef_file_path)
            convert_tiff_to_png(tiff_file_path, png_file_path)
            
            os.remove(tiff_file_path)

    print("Conversion completed.")

def main():
    input_folder_path = input("Please enter the path to the folder containing the NEF files: ").strip().strip("'\"")
    
    if os.path.isdir(input_folder_path):
        process_folder(input_folder_path)
    else:
        print("The provided path does not exist or is not a directory. Please run the script again with a valid path.")

if __name__ == "__main__":
    main()
