from tkinter import *
from tkinter import ttk
from utils.converter import formats
from functions import pick_files, start_conversion


d_font = font=('Arial', 20, "bold")

def generate_program_window():

    # Create frame instance
    main_window = Tk()

    # Set frame geometry
    main_window.geometry("750x450")

    frame = LabelFrame(main_window, width=650, height=350, bd=0, background='black')
    frame.grid(column=0, row=0, columnspan=2, rowspan=4, padx=50, pady=50)

    Label(main_window, text="Python-based image converter", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=0, columnspan=2)

    Label(main_window, text="Convert images to: ", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=1, sticky=E)
    format_selection = ttk.Combobox(
        state='readonly',
        values=formats,
    )
    format_selection.set('.jpg')
    format_selection.grid(column=1, row=1, sticky=W)

    img_window_message = Label(main_window, text="No files selected", anchor='nw', justify='left')
    img_window_message.grid(column=0, row=2, columnspan=2, sticky='NSEW')

    ttk.Button(main_window, text = "Select Image(s)", command = pick_files(main_window, img_window_message)).grid(column=0, row=3, sticky='NSEW', padx=20, pady=20)

    ttk.Button(main_window, text="Convert Image(s) =>", command = start_conversion(format_selection, main_window, img_window_message)).grid(column=1, row=3, sticky='NSEW', padx=20, pady=20)
    main_window.configure(background='black')
    main_window.mainloop()

if __name__ == "__main__":
    generate_program_window()