from tkinter import X, BOTTOM
from tkinter.ttk import Frame, Label
from .styles import layout


def Footer(main_window, text="Supports 20+ image formats including JPG, PNG, HEIC, WebP, and more"):
    """
    Create a footer component with information text.
    
    Args:
        main_window: The main application window
        text: The text to display in the footer (optional)
    """
    footer_frame = Frame(
        main_window,
        style='Footer.TFrame',
        height=layout.FOOTER_HEIGHT)
    
    footer_frame.pack(fill=X, side=BOTTOM)
    footer_frame.pack_propagate(False)
    
    footer_label = Label(
        footer_frame,
        text=text,
        style='FooterText.TLabel')
    
    footer_label.pack(pady=layout.FOOTER_PADDING)