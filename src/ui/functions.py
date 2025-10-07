
import os
from dotenv import load_dotenv
from tkinter.filedialog import askopenfilenames
from utils.converter import RGBImageConverter, formats

load_dotenv()

def pick_files(window, message):
    global paths
    types = [("Image file", format) for format in formats]
    paths = [file.strip() for file in askopenfilenames(parent=window, title="Select the images you want to convert", filetypes=types)]
    new_message = ''
    for p in paths:
        new_message += p.split('/')[-1].strip() + '\n'
    if new_message != '':
        message.config(text= new_message)
    return paths

def start_conversion(selection, window, message):
    global paths
    global converter

    converter = RGBImageConverter(selection.get(), os.getenv('OUT_DIR'))
    message.config(text = 'Converting image(s).')
    window.update()
    tail_recusive_convert(paths)


def tail_recusive_convert(window, message, remaining_paths):
    global paths
    global converter

    if len(remaining_paths) == 0:
        paths = []
        del converter
        message.config(text = 'Finished converting image(s).')
        window.update()
    else:
        converter.convert_image(remaining_paths[0])
        message.config(text = message['text'] + '.')
        window.update()
        tail_recusive_convert(remaining_paths[1:])