from types import SimpleNamespace
from tkinter import ttk, FLAT

colors = SimpleNamespace(
    BG_PRIMARY = "#000000",
    BG_SECONDARY = "#3d3d3d",
    ACCENT_COLOR = "#474747",
    ACCENT_HOVER = "#5e5e5e",
    TEXT_PRIMARY = "#00aa00",
    TEXT_SECONDARY = "#00ff00",
    BORDER_COLOR = "#9B9B9B",
    FILE_LIST_BG = "#f8f9fa",
    FILE_LIST_FG = "black",
)

fonts = SimpleNamespace(
    HEADER = ('Courier', 28, 'bold'),
    TEXT = ('Courier', 14, 'bold'),
    SUBTEXT = ('Courier', 10, 'bold'),
    FILE_LIST = ('Consolas', 10),
)

layout = SimpleNamespace(
    FOOTER_HEIGHT = 40,
    FOOTER_PADDING = 10,
    FILE_LIST_HEIGHT = 8,
    FILE_LIST_PADDING = 15,
    CARD_PADDING_X = 30,
    CARD_PADDING_Y = (20, 10),
    LIST_PADDING_Y = (0, 20),
    FILE_COUNT_PADDING = (10, 0),
    CARD_BOTTOM_MARGIN = (0, 20),
)

def default_style() -> ttk.Style:
    style = ttk.Style()
    style.theme_use('default')

    # Main Content Frame Styles
    style.configure('Content.TFrame',
                    background=colors.BG_PRIMARY)

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
    style.configure('FileCard.TFrame',
                    background=colors.BG_SECONDARY,
                    relief=FLAT,
                    borderwidth=1,
                    lightcolor=colors.BORDER_COLOR,
                    darkcolor=colors.BORDER_COLOR)
    
    style.configure('FileHeader.TFrame',
                    background=colors.BG_SECONDARY)
    
    style.configure('FileLabel.TLabel',
                    font=fonts.TEXT,
                    background=colors.BG_SECONDARY,
                    foreground=colors.TEXT_PRIMARY)
    
    style.configure('FileCount.TLabel',
                    font=fonts.SUBTEXT,
                    background=colors.BG_SECONDARY,
                    foreground=colors.TEXT_SECONDARY)
    
    style.configure('ListContainer.TFrame',
                    background=colors.BG_SECONDARY)
    
    # Scrollbar Styles
    style.configure('FileList.Vertical.TScrollbar',
                    background=colors.BG_SECONDARY,
                    darkcolor=colors.BORDER_COLOR,
                    lightcolor=colors.BG_SECONDARY,
                    troughcolor=colors.BG_SECONDARY,
                    bordercolor=colors.BORDER_COLOR,
                    arrowcolor=colors.TEXT_SECONDARY,
                    gripcount=0)
    
    # Footer Styles
    style.configure('Footer.TFrame',
                    background=colors.BG_PRIMARY)
    
    style.configure('FooterText.TLabel',
                    font=fonts.SUBTEXT,
                    background=colors.BG_PRIMARY,
                    foreground=colors.TEXT_SECONDARY)
    
    # Button Styles
    style.configure('ButtonFrame.TFrame',
                    background=colors.BG_PRIMARY)
    
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