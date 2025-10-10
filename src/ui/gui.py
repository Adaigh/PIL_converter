"""
PIL Image Converter - GUI Interface

This module provides the graphical user interface for the image converter application
using the Tkinter library. It creates a simple, user-friendly interface that allows
users to select images, choose output formats, and initiate batch conversions.

GUI Components:
- Format selection dropdown with all supported image formats
- File selection button for choosing input images
- Convert button to start the conversion process
- Status display showing selected files and conversion progress
- Styled interface with custom fonts and colors

The interface is designed to be intuitive and provides real-time feedback
during the conversion process.

Functions:
    generate_program_window(): Creates and displays the main application window

Author: Adaigh
Project: PIL_converter
Date: 2025
"""

from tkinter import Tk, BOTH
from tkinter.ttk import Frame

from .components.header import Header
from .components.format_selector import FormatSelector
from .components.file_selection import FileSelection
from .components.action_buttons import ActionButtons
from .components.footer import Footer
from .components.window_setup import setup_window, center_window
from .components.styles import colors


def generate_program_window():
    """Generate and display the main application window with professional styling."""
    
    # Create main window
    main_window = Tk()
    
    # Setup window properties and styling
    setup_window(main_window)
    
    # ==================== HEADER SECTION ====================
    Header(
        main_window,
        title='Image Format Converter',
        subtitle='Convert your images between multiple formats quickly and easily'
    )
    
    # ==================== MAIN CONTENT AREA ====================
    content_frame = Frame(main_window, style='Content.TFrame')
    content_frame.pack(fill=BOTH, expand=True, padx=40, pady=30)
    
    # Format Selection Component
    format_selection = FormatSelector(content_frame, "Select the output format:")
    
    # File Selection Component
    file_list_text, file_count_label = FileSelection(content_frame)
    
    # Action Buttons Component
    select_button, convert_button = ActionButtons(
        content_frame, main_window, file_list_text, file_count_label, format_selection
    )
    
    # ==================== FOOTER ====================
    Footer(main_window)
    
    # Center window on screen and start main loop
    center_window(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    generate_program_window()
