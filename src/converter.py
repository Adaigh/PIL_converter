from PIL import Image
from pillow_heif import register_heif_opener
from dotenv import load_dotenv
import os

def convert_images(files, extension):
    load_dotenv()
    register_heif_opener()
    for path in files:
        image = Image.open(path)
        filename = path.split('/')[-1]
        outfile_name = filename.split('.')[0] + extension
        output_directory = os.getenv('OUT_DIR')
        image.save(output_directory + outfile_name)