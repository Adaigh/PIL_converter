from tkinter import Frame, Text, X, Y, LEFT, RIGHT, BOTH, FLAT, DISABLED, NORMAL, END
from tkinter.ttk import Label, Scrollbar, Frame as TTKFrame
from .styles import colors, fonts, layout


def FileSelection(content_frame):
    """
    Create a file selection card component that displays selected files.
    
    Args:
        content_frame: The parent frame to attach this component to
        
    Returns:
        tuple: (file_list_text, file_count_label) - The text widget and count label for external updates
    """
    file_card = Frame(
        content_frame,
        bg=colors.BG_SECONDARY,
        relief=FLAT,
        bd=1,
        highlightbackground=colors.BORDER_COLOR,
        highlightthickness=1)
    
    file_card.pack(fill=BOTH, expand=True, pady=layout.CARD_BOTTOM_MARGIN)
    
    file_header = TTKFrame(
        file_card,
        style='FileHeader.TFrame')
    
    file_header.pack(fill=X, padx=layout.CARD_PADDING_X, pady=layout.CARD_PADDING_Y)
    
    file_label = Label(
        file_header,
        text="Selected Files:",
        style='FileLabel.TLabel')
    
    file_label.pack(side=LEFT)
    
    file_count_label = Label(
        file_header,
        text="(0 files)",
        style='FileCount.TLabel')
    
    file_count_label.pack(side=LEFT, padx=layout.FILE_COUNT_PADDING)
    
    list_container = TTKFrame(
        file_card,
        style='ListContainer.TFrame')
    
    list_container.pack(fill=BOTH, expand=True, padx=layout.CARD_PADDING_X, pady=layout.LIST_PADDING_Y)
    
    scrollbar = Scrollbar(
        list_container,
        style='FileList.Vertical.TScrollbar')
    
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Text widget for file list
    file_list_text = Text(list_container,
                         height=layout.FILE_LIST_HEIGHT,
                         font=fonts.FILE_LIST,
                         bg=colors.FILE_LIST_BG,
                         fg=colors.FILE_LIST_FG,
                         relief=FLAT,
                         bd=0,
                         padx=layout.FILE_LIST_PADDING,
                         pady=layout.FILE_LIST_PADDING,
                         yscrollcommand=scrollbar.set,
                         state=DISABLED,
                         wrap=None)
    
    file_list_text.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=file_list_text.yview)
    
    # Initial message
    file_list_text.config(state=NORMAL)
    file_list_text.insert(1.0, "No files selected yet.\n\nClick 'Select Images' to choose files for conversion.")
    file_list_text.tag_configure('center', justify='center', foreground=colors.FILE_LIST_FG)
    file_list_text.tag_add('center', 1.0, END)
    file_list_text.config(state=DISABLED)
    
    return file_list_text, file_count_label