"""
PIL Image Converter - Core Conversion Utilities

This module contains the RGBImageConverter class, which provides the core functionality
for converting images between different formats using the PIL (Pillow) library.

The converter handles:
- Multiple input/output formats (24+ supported formats)
- HEIF/HEIC format support via pillow-heif
- Automatic transparency handling (RGBA to RGB conversion for JPEG output)
- Input validation and error handling
- Flexible output directory configuration

Supported Formats:
    Input/Output: JPG, JPEG, PNG, BMP, HEIC, HEIF, BLP, DDS, DIB, EPS, GIF,
                  ICNS, ICO, IM, MSP, PCX, PFM, PPM, TGA, TIFF, WebP

Classes:
    RGBImageConverter: Main converter class with format conversion capabilities

Author: Adaigh
Project: PIL_converter
Date: 2025
"""

from PIL import Image
from pillow_heif import register_heif_opener

formats = ['.jpg', '.jpeg', '.png', '.bmp', '.heic', '.heif', '.blp', '.dds', '.dib', '.eps', '.gif', '.icns', '.ico', '.im', '.msp', '.pcx', '.pfm', '.ppm', '.tga', '.tiff', '.webp']

class RGBImageConverter:
    def __init__(self, img_format:str = None, output_directory: str = None):
        self.out_dir = output_directory      
        self.heif_registered = False
        if img_format in formats:
            self.img_format = img_format
    
    def set_output_directory(self, output_directory: str):
        if type(output_directory) == str:
            self.out_dir = output_directory

    def set_format(self, format_string: str):
        if format_string in formats:
            self.img_format = format_string

    # Main working function
    def convert_image(self, absolute_path):
        self.validate_output_requirements()
        name, extension = self.extract_img_data(absolute_path)
        self.activate_heif(extension)
        image = Image.open(absolute_path)
        image = self.handle_transparency(image)
        outfile_name = name + self.img_format
        image.save(self.out_dir + outfile_name)

    def extract_img_data(self, path):
        name, extension = path.split('/')[-1].split('.')
        self.validate_input_extension(name, extension)
        return name, extension
    
    def activate_heif(self, extension):
        if extension.lower() in ['heif', 'heic'] and not self.heif_registered:
            register_heif_opener()
            self.heif_registered = True

    def handle_transparency(self, img):
        # convert RGBA to RGB
        if img.mode == "RGBA" and self.img_format in ['.jpg', '.jpeg']:
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.getchannel('A'))
            return background
        return img
    
    def validate_output_requirements(self):
        # output format validation
        if self.img_format is None:
            raise ValueError("RGBImageConverter output format not set")
        if self.img_format not in formats:
            raise ValueError("Invalid output format")
        if self.out_dir is None:
            raise ValueError("Invalid output directory")
        
    def validate_input_extension(self, name, extension):
        # input format validation
        if f".{extension.lower()}" not in formats:
            raise ValueError(f"Input image format unsupported: {'.'.join([name, extension])}")