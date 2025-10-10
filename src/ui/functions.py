
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
from tkinter import messagebox, NORMAL, DISABLED, END
from dotenv import load_dotenv
from tkinter.filedialog import askopenfilenames
from utils.converter import RGBImageConverter, formats

load_dotenv()

# Global state for selected files
paths = []


def pick_files(window, file_display, count_label):
    """
    Open file dialog for selecting image files and update UI with selections.
    
    Args:
        window: Parent Tkinter window
        file_display: Text widget to display selected files
        count_label: Label widget to show file count
    
    Returns:
        List of selected file paths
    """
    global paths
    
    types = [("Image files", " ".join([f"*{format}" for format in formats])),
             ("All files", "*.*")]
    
    selected = askopenfilenames(
        parent=window,
        title="Select images to convert",
        filetypes=types
    )
    
    if selected:
        paths = [file.strip() for file in selected]
        
        # Update file display
        file_display.config(state=NORMAL)
        file_display.delete(1.0, END)
        
        for i, path in enumerate(paths, 1):
            filename = path.split('/')[-1].strip()
            file_display.insert(END, f"{i}. {filename}\n")
        
        file_display.config(state=DISABLED)
        
        # Update count label
        count_label.config(text=f"({len(paths)} file{'s' if len(paths) != 1 else ''})")
    
    return paths


def start_conversion(format_selection, window, status_display, convert_button, select_button):
    """
    Start the image conversion process for all selected files.
    
    Args:
        format_selection: Combobox widget containing selected output format
        window: Parent Tkinter window
        status_display: Text widget to show conversion progress
        convert_button: Convert button widget (to disable during conversion)
        select_button: Select button widget (to disable during conversion)
    """
    global paths
    
    if not paths:
        messagebox.showwarning(
            "No Files Selected",
            "Please select at least one image file to convert."
        )
        return
    
    output_dir = os.getenv('OUT_DIR')
    if not output_dir:
        messagebox.showerror(
            "Configuration Error",
            "Output directory not configured. Please set OUT_DIR in your .env file."
        )
        return
    
    # Validate output directory exists
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            messagebox.showerror(
                "Directory Error",
                f"Could not create output directory:\n{output_dir}\n\nError: {str(e)}"
            )
            return
    
    selected_format = format_selection.get()
    
    # Disable buttons during conversion
    convert_button.config(state=DISABLED)
    select_button.config(state=DISABLED)
    
    # Initialize converter
    converter = RGBImageConverter(selected_format, output_dir)
    
    # Update status display
    status_display.config(state=NORMAL)
    status_display.delete(1.0, END)
    status_display.insert(1.0, "Starting conversion...\n\n")
    status_display.config(state=DISABLED)
    window.update()
    
    # Convert each file
    successful = 0
    failed = 0
    errors = []
    
    for i, path in enumerate(paths, 1):
        filename = path.split('/')[-1].strip()
        
        # Update progress
        status_display.config(state=NORMAL)
        status_display.insert(END, f"[{i}/{len(paths)}] Converting: {filename}...")
        status_display.config(state=DISABLED)
        status_display.see(END)
        window.update()
        
        try:
            converter.convert_image(path)
            successful += 1
            
            status_display.config(state=NORMAL)
            status_display.insert(END, " ✓ Done\n")
            status_display.config(state=DISABLED)
            
        except Exception as e:
            failed += 1
            error_msg = str(e)
            errors.append((filename, error_msg))
            
            status_display.config(state=NORMAL)
            status_display.insert(END, f" ✗ Failed\n")
            status_display.config(state=DISABLED)
        
        status_display.see(END)
        window.update()
    
    # Show completion message
    status_display.config(state=NORMAL)
    status_display.insert(END, f"\n{'='*50}\n")
    status_display.insert(END, f"Conversion complete!\n")
    status_display.insert(END, f"Successful: {successful} | Failed: {failed}\n")
    
    if output_dir:
        status_display.insert(END, f"\nOutput location: {output_dir}\n")
    
    status_display.config(state=DISABLED)
    status_display.see(END)
    
    # Re-enable buttons
    convert_button.config(state=NORMAL)
    select_button.config(state=NORMAL)
    
    # Show summary dialog
    if failed > 0:
        error_details = "\n".join([f"• {fname}: {err[:50]}..." for fname, err in errors[:5]])
        if len(errors) > 5:
            error_details += f"\n... and {len(errors) - 5} more"
        
        messagebox.showwarning(
            "Conversion Complete with Errors",
            f"Successfully converted: {successful} file(s)\n"
            f"Failed: {failed} file(s)\n\n"
            f"Errors:\n{error_details}"
        )
    else:
        messagebox.showinfo(
            "Conversion Complete",
            f"Successfully converted {successful} file(s) to {selected_format} format!\n\n"
            f"Location: {output_dir}"
        )
    
    # Clear paths after conversion
    paths = []

