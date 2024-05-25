import sys
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            print(f"No EXIF data found in {image_path}")
            return
        
        exif_info = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            exif_info[tag_name] = value
        
        return exif_info
    except Exception as e:
        print(f"Error reading EXIF data from {image_path}: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python read_exif.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    exif_data = get_exif_data(image_path)
    if exif_data:
        print(f"EXIF data for {image_path}:")
        for tag, value in exif_data.items():
            print(f"{tag}: {value}")
