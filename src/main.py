"""
PIL Image Converter - Main Entry Point

A Python-based image converter application that provides a simple GUI interface
for converting images between various formats using the PIL (Pillow) library.

This application supports a wide range of image formats including:
- Common formats: JPG, PNG, BMP, TIFF, WebP, GIF
- HEIC/HEIF (Apple formats)
- Specialized formats: BLP, DDS, EPS, ICNS, ICO, and more

Features:
- User-friendly Tkinter GUI
- Batch conversion support
- Automatic transparency handling (RGBA to RGB conversion)
- HEIF format support via pillow-heif

Author: Adaigh
Project: PIL_converter
Date: 2025

Usage:
    Run this script to launch the GUI application:
    python main.py
"""

from ui.gui import generate_program_window 

if __name__ == "__main__":
    generate_program_window()