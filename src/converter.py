from PIL import Image
from pillow_heif import register_heif_opener

formats = ['.jpg', '.jpeg', '.png', '.bmp', '.heic', '.heif', '.blp', '.dds', '.dib', '.eps', '.gif', '.icns', '.ico', '.im', '.msp', '.pcx', '.pfm', '.ppm', '.tga', '.tiff', '.webp']

class RGBImageConverter():
    def __init__(self, img_format:str = None, output_directory: str = None):
        self.out_dir = output_directory      
        self.registered = False
        if img_format in formats:
            self.img_format = img_format
    
    def set_output_directory(self, output_directory: str):
        if type(output_directory) == str:
            self.out_dir = output_directory
    
    def activate_heif(self):
        if not self.registered:
            register_heif_opener()
            self.registered = True

    def set_format(self, format_string:str):
        if format_string in formats:
            self.img_format = format_string

    # Main working function
    def convert_image(self, absolute_path):

        # output format validation
        if self.img_format is None:
            raise ValueError("RGBImageConverter output format not set")
        if self.img_format not in formats:
            raise ValueError("Invalid output format")
        if self.out_dir is None:
            raise ValueError("Invalid output directory")
        
        # extract filename and extension from path
        name, extension = absolute_path.split('/')[-1].split('.')
        
        # input format validation
        if f".{extension.lower()}" not in formats:
            raise ValueError(f"Input image format unsupported: {'.'.join([name, extension])}")
        
        # auto-activate heif conversion
        if extension.lower() in ['heif', 'heic']:
            self.activate_heif()

        # open image
        image = Image.open(absolute_path)

        # convert RGBA to RGB
        if image.mode == "RGBA":
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask=image.getchannel('A'))
            image = background
        
        # Build output file name with extension
        outfile_name = name + self.img_format

        # PIL auto-detecting save format
        image.save(self.out_dir + outfile_name)