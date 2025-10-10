from tkinter import X, LEFT
from tkinter.ttk import Frame, Button
from ..functions import pick_files, start_conversion


def ActionButtons(content_frame, main_window, file_list_text, file_count_label, format_selection):
    """
    Create action buttons component with Select Images and Convert Images buttons.
    
    Args:
        content_frame: The parent frame to attach this component to
        main_window: The main application window
        file_list_text: The text widget displaying selected files
        file_count_label: The label showing file count
        format_selection: The format selector widget
        
    Returns:
        tuple: (select_button, convert_button) - The button widgets for external access
    """
    
    # -------------------- Action Buttons --------------------
    button_frame = Frame(
        content_frame,
        style='ButtonFrame.TFrame')
    
    button_frame.pack(fill=X)
    
    select_button = Button(
        button_frame,
        text="📁  Select Images",
        style='Accent.TButton',
        command=lambda: pick_files(main_window, file_list_text, file_count_label))
    
    select_button.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))
    
    convert_button = Button(
        button_frame,
        text="✓  Convert Images",
        style='Accent.TButton',
        command=lambda: start_conversion(format_selection, main_window, file_list_text, convert_button, select_button))
    
    convert_button.pack(side=LEFT, fill=X, expand=True, padx=(10, 0))
    
    return select_button, convert_button