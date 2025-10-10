from tkinter import X
from tkinter.ttk import Frame, Label

def Header(main_window, title, subtitle) -> None:
    """
    Create a the program header component.
    
    Args:
        main_window: The main application window
        title: The text for the main title
        subtitle: The text for the header subtitle
    """
    header_frame = Frame(
        main_window,
        style='Header.TFrame',
        height=100)
    
    header_frame.pack(fill=X)
    header_frame.pack_propagate(False)
    
    # Title
    title_label = Label(header_frame, 
                       text=title,
                       style='Title.TLabel')
    title_label.pack(pady=(20, 5))
    
    # Subtitle
    subtitle_label = Label(header_frame,
                          text=subtitle,
                          style='Subtitle.TLabel')
    subtitle_label.pack()