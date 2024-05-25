import os
import sys
from PIL import Image

def remove_exif_from_image(image_path):
    try:
        image = Image.open(image_path)
        # Usuwamy dane EXIF zapisując obraz w nowym pliku bez tych danych
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save(image_path)
        print(f"Removed EXIF data from {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def remove_exif_from_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'tiff')):
                file_path = os.path.join(root, file)
                remove_exif_from_image(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_exif.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    if not os.path.isdir(directory_path):
        print(f"The provided path '{directory_path}' is not a directory.")
        sys.exit(1)
    
    remove_exif_from_directory(directory_path)
