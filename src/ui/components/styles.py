from types import SimpleNamespace
from tkinter import ttk, FLAT
    # Color scheme
colors = SimpleNamespace(
    BG_PRIMARY = "#000000",
    BG_SECONDARY = "#3d3d3d",
    ACCENT_COLOR = "#474747",
    ACCENT_HOVER = "#5e5e5e",
    TEXT_PRIMARY = "#00aa00",
    TEXT_SECONDARY = "#00ff00",
    BORDER_COLOR = "#9B9B9B",
)

fonts = SimpleNamespace(
    HEADER = ('Courier', 28, 'bold'),
    TEXT = ('Courier', 14, 'bold'),
    SUBTEXT = ('Courier', 10, 'bold'),
)

def default_style() -> ttk.Style:
    style = ttk.Style()
    style.theme_use('default')

    # Header Styles
    style.configure('Header.TFrame',
                    background=colors.BG_PRIMARY)

    style.configure('Title.TLabel',
                    font=fonts.HEADER,
                    background=colors.BG_PRIMARY,
                    foreground=colors.TEXT_PRIMARY)
    
    style.configure('Subtitle.TLabel',
                    font=fonts.TEXT,
                    background=colors.BG_PRIMARY,
                    foreground=colors.TEXT_SECONDARY)
    
    # Format Selector Styles
    style.configure('Card.TFrame',
                    background=colors.BG_SECONDARY,
                    relief=FLAT,
                    borderwidth=1)
    
    style.configure('Inner.TFrame',
                    background=colors.BG_SECONDARY)
    
    style.configure('Text.TLabel',
                    font=fonts.TEXT,
                    background=colors.BG_SECONDARY,
                    foreground=colors.TEXT_PRIMARY)
    
    style.configure('Selector.TCombobox',
                    fieldbackground=colors.BG_SECONDARY,
                    background=colors.BG_SECONDARY,
                    borderwidth=1,
                    relief='solid',
                    font=fonts.TEXT)
    
    # File Selection Styles

    
    
    # Configure button style
    style.configure('Accent.TButton',
                   background=colors.ACCENT_COLOR,
                   foreground=colors.TEXT_SECONDARY,
                   borderwidth=0,
                   focuscolor='none',
                   font=fonts.TEXT,
                   padding=(20, 12))
    
    style.map('Accent.TButton',
             background=[
                 ('active', colors.ACCENT_HOVER),
                 ('pressed', colors.ACCENT_HOVER)
                 ])
    
    # Configure combobox style
    style.configure('TCombobox',
                   fieldbackground=colors.BG_SECONDARY,
                   background=colors.BG_SECONDARY,
                   borderwidth=1,
                   relief='solid',
                   font=fonts.TEXT)