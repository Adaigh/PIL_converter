from .styles import colors, default_style


def setup_window(main_window):
    """
    Configure the main window properties and styling.
    
    Args:
        main_window: The main Tkinter window to configure
    """
    
    main_window.title("Image Format Converter")
    main_window.geometry("900x650")
    main_window.resizable(False, False)
    main_window.configure(bg=colors.BG_PRIMARY)
    
    # Apply default styling
    default_style()


def center_window(main_window):
    """
    Center the window on the screen.
    
    Args:
        main_window: The main Tkinter window to center
    """
    
    main_window.update_idletasks()
    width = main_window.winfo_width()
    height = main_window.winfo_height()
    x = (main_window.winfo_screenwidth() // 2) - (width // 2)
    y = (main_window.winfo_screenheight() // 2) - (height // 2)
    main_window.geometry(f'{width}x{height}+{x}+{y}')