from tkinter import X, LEFT
from tkinter.ttk import Frame, Label, Combobox

from utils.converter import formats

def FormatSelector(content_frame, label_text):

    format_card = Frame(
        content_frame,
        style='Card.TFrame')
    
    format_card.pack(fill=X, pady=(0, 20))
    
    format_inner = Frame(
        format_card,
        style='Inner.TFrame')
    
    format_inner.pack(padx=30, pady=25)
    
    format_label = Label(
        format_inner,
        text=label_text,
        style='Text.TLabel')
    
    format_label.pack(side=LEFT, padx=(0, 15))
    
    format_selection = Combobox(
        format_inner,
        state='readonly',
        values=formats,
        width=10,
        style='Selector.TCombobox')
    
    format_selection.set('.jpg')
    format_selection.pack(side=LEFT)

    return format_selection