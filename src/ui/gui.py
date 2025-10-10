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

from tkinter import *
from tkinter import ttk

from .components.styles import colors, fonts, default_style
from .components.header import Header
from .components.format_selector import FormatSelector
from .functions import pick_files, start_conversion


def generate_program_window():
    """Generate and display the main application window with professional styling."""
    
    # Create main window
    main_window = Tk()
    main_window.title("Image Format Converter")
    main_window.geometry("900x650")
    main_window.resizable(False, False)

    main_window.configure(bg=colors.BG_PRIMARY)

    default_style()
    
    # Custom style for ttk widgets
    # style = ttk.Style()
    # style.theme_use('clam')
    
    # # Configure button style
    # style.configure('Accent.TButton',
    #                background=colors.ACCENT_COLOR,
    #                foreground=colors.TEXT_SECONDARY,
    #                borderwidth=0,
    #                focuscolor='none',
    #                font=('Segoe UI', 11, 'bold'),
    #                padding=(20, 12))
    # style.map('Accent.TButton',
    #          background=[('active', colors.ACCENT_HOVER), ('pressed', colors.ACCENT_HOVER)])
    
    # # Configure combobox style
    # style.configure('TCombobox',
    #                fieldbackground=colors.BG_SECONDARY,
    #                background=colors.BG_SECONDARY,
    #                borderwidth=1,
    #                relief='solid',
    #                font=('Segoe UI', 10))
    
    # ==================== HEADER SECTION ====================
    Header(
        main_window,
        title='Image Format Converter',
        subtitle='Convert your images between multiple formats quickly and easily'
    )
    
    # header_frame = Frame(main_window, bg=colors.BG_PRIMARY, height=100)
    # header_frame.pack(fill=X)
    # header_frame.pack_propagate(False)
    
    # # Title
    # title_label = Label(header_frame, 
    #                    text="Image Format Converter",
    #                    font=fonts.HEADER,
    #                    bg=colors.BG_PRIMARY,
    #                    fg=colors.TEXT_PRIMARY)
    # title_label.pack(pady=(20, 5))
    
    # # Subtitle
    # subtitle_label = Label(header_frame,
    #                       text="Convert your images between multiple formats quickly and easily",
    #                       font=('Segoe UI', 11),
    #                       bg=colors.BG_PRIMARY,
    #                       fg=colors.TEXT_SECONDARY)
    # subtitle_label.pack()
    
    # ==================== MAIN CONTENT AREA ====================
    content_frame = Frame(main_window, bg=colors.BG_PRIMARY)
    content_frame.pack(fill=BOTH, expand=True, padx=40, pady=30)
    
    format_selection = FormatSelector(content_frame, "Select the output format:")

    # # -------------------- Format Selection Card --------------------
    # format_card = Frame(content_frame, bg=colors.BG_SECONDARY, relief=FLAT, bd=1, highlightbackground=colors.BORDER_COLOR, highlightthickness=1)
    # format_card.pack(fill=X, pady=(0, 20))
    
    # format_inner = Frame(format_card, bg=colors.BG_SECONDARY)
    # format_inner.pack(padx=30, pady=25)
    
    # format_label = Label(format_inner,
    #                     text="Output Format:",
    #                     font=('Segoe UI', 13, 'bold'),
    #                     bg=colors.BG_SECONDARY,
    #                     fg=colors.TEXT_PRIMARY)
    # format_label.pack(side=LEFT, padx=(0, 15))
    
    # format_selection = ttk.Combobox(format_inner,
    #                                state='readonly',
    #                                values=formats,
    #                                width=15,
    #                                font=('Segoe UI', 11))
    # format_selection.set('.jpg')
    # format_selection.pack(side=LEFT)
    
    # format_help = Label(format_inner,
    #                    text="Select the desired output format for your images",
    #                    font=('Segoe UI', 9),
    #                    bg=colors.BG_SECONDARY,
    #                    fg=colors.TEXT_SECONDARY)
    # format_help.pack(side=LEFT, padx=(20, 0))
    
    # -------------------- File Selection Card --------------------
    file_card = Frame(content_frame, bg=colors.BG_SECONDARY, relief=FLAT, bd=1, highlightbackground=colors.BORDER_COLOR, highlightthickness=1)
    file_card.pack(fill=BOTH, expand=True, pady=(0, 20))
    
    file_header = Frame(file_card, bg=colors.BG_SECONDARY)
    file_header.pack(fill=X, padx=30, pady=(20, 10))
    
    file_label = Label(file_header,
                      text="Selected Files:",
                      font=('Segoe UI', 13, 'bold'),
                      bg=colors.BG_SECONDARY,
                      fg=colors.TEXT_PRIMARY)
    file_label.pack(side=LEFT)
    
    file_count_label = Label(file_header,
                            text="(0 files)",
                            font=('Segoe UI', 10),
                            bg=colors.BG_SECONDARY,
                            fg=colors.TEXT_SECONDARY)
    file_count_label.pack(side=LEFT, padx=(10, 0))
    
    # Scrollable file list with frame
    list_container = Frame(file_card, bg=colors.BG_SECONDARY)
    list_container.pack(fill=BOTH, expand=True, padx=30, pady=(0, 20))
    
    # Scrollbar
    scrollbar = Scrollbar(list_container)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Text widget for file list
    file_list_text = Text(list_container,
                         height=8,
                         font=('Consolas', 10),
                         bg='#f8f9fa',
                         fg='black',
                         relief=FLAT,
                         bd=0,
                         padx=15,
                         pady=15,
                         yscrollcommand=scrollbar.set,
                         state=DISABLED,
                         wrap=NONE)
    file_list_text.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=file_list_text.yview)
    
    # Initial message
    file_list_text.config(state=NORMAL)
    file_list_text.insert(1.0, "No files selected yet.\n\nClick 'Select Images' to choose files for conversion.")
    file_list_text.tag_configure('center', justify='center', foreground='black')
    file_list_text.tag_add('center', 1.0, END)
    file_list_text.config(state=DISABLED)
    
    # -------------------- Action Buttons --------------------
    button_frame = Frame(content_frame, bg=colors.BG_PRIMARY)
    button_frame.pack(fill=X)
    
    select_button = ttk.Button(button_frame,
                              text="📁  Select Images",
                              style='Accent.TButton',
                              command=lambda: pick_files(main_window, file_list_text, file_count_label))
    select_button.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
    
    convert_button = ttk.Button(button_frame,
                               text="✓  Convert Images",
                               style='Accent.TButton',
                               command=lambda: start_conversion(format_selection, main_window, file_list_text, convert_button, select_button))
    convert_button.pack(side=LEFT, fill=X, expand=True, padx=(10, 0))
    
    # ==================== FOOTER ====================
    footer_frame = Frame(main_window, bg=colors.BG_PRIMARY, height=40)
    footer_frame.pack(fill=X, side=BOTTOM)
    footer_frame.pack_propagate(False)
    
    footer_label = Label(footer_frame,
                        text="Supports 20+ image formats including JPG, PNG, HEIC, WebP, and more",
                        font=('Segoe UI', 9),
                        bg=colors.BG_PRIMARY,
                        fg=colors.TEXT_SECONDARY)
    footer_label.pack(pady=10)
    
    # Center window on screen
    main_window.update_idletasks()
    width = main_window.winfo_width()
    height = main_window.winfo_height()
    x = (main_window.winfo_screenwidth() // 2) - (width // 2)
    y = (main_window.winfo_screenheight() // 2) - (height // 2)
    main_window.geometry(f'{width}x{height}+{x}+{y}')
    
    main_window.mainloop()


if __name__ == "__main__":
    generate_program_window()
