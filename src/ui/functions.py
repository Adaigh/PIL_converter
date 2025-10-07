
"""
PIL Image Converter - UI Support Functions

This module contains helper functions that support the GUI interface by handling
file operations, user interactions, and the conversion workflow. These functions
bridge the gap between the user interface and the core conversion logic.

Key Functions:
- File selection dialog integration
- Batch conversion processing with progress updates
- Environment configuration loading
- UI state management during conversions

The module uses a global state approach to manage file paths and converter instances
across the conversion workflow, providing seamless integration between user actions
and backend processing.

Functions:
    pick_files(): Opens file dialog for image selection
    start_conversion(): Initiates the conversion process with selected parameters

Dependencies:
    - Environment variables via .env file for output directory configuration
    - RGBImageConverter for actual image processing
    - Tkinter for file dialog integration

Author: Adaigh
Project: PIL_converter
Date: 2025
"""

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

    def tail_recusive_convert(remaining_paths):
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

    converter = RGBImageConverter(selection.get(), os.getenv('OUT_DIR'))
    message.config(text = 'Converting image(s).')
    window.update()
    tail_recusive_convert(paths)


