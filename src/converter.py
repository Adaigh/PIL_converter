from PIL import Image
from pillow_heif import register_heif_opener
from dotenv import load_dotenv
import os

def convert_images(files, format):
    load_dotenv()
    register_heif_opener()
    for path in files:
        image = Image.open(path)
        filename = path.split('/')[-1].split('.')
        name, extension = filename[0], filename[1]
        if image.mode == "RGBA":
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.getchannel('A'))
            image = background
        outfile_name = name + format
        output_directory = os.getenv('OUT_DIR')
        image.save(output_directory + outfile_name, quality=50)