"""
UI Components Package

This package contains modular GUI components for the PIL Image Converter application.
Each component is designed to be self-contained and reusable.

Components:
- header: Application title and subtitle
- format_selector: Dropdown for selecting output image format
- file_selection: File list display with scrolling
- action_buttons: Select and Convert action buttons
- footer: Application information footer
- window_setup: Window configuration utilities
- styles: Color scheme and styling definitions
"""

from .header import Header
from .format_selector import FormatSelector
from .file_selection import FileSelection
from .action_buttons import ActionButtons
from .footer import Footer
from .window_setup import setup_window, center_window
from .styles import colors, fonts, layout, default_style

__all__ = [
    'Header',
    'FormatSelector', 
    'FileSelection',
    'ActionButtons',
    'Footer',
    'setup_window',
    'center_window',
    'colors',
    'fonts',
    'layout',
    'default_style'
]