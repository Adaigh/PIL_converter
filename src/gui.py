from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from converter import convert_images


formats = ['.jpg', '.jpeg', '.png', '.bmp', '.heic', '.heif', '.blp', '.dds', '.dib', '.eps', '.gif', '.icns', '.ico', '.im', '.msp', '.pcx', '.pfm', '.ppm', '.tga', '.tiff', '.webp']
types = [("Image file", format) for format in formats]
d_font = font=('Arial', 20, "bold")
paths = []

def generate_program_window():

    def pickFiles():
        global paths
        paths = [file.strip() for file in askopenfilenames(parent=window, title="Select the images you want to convert", filetypes=types)]
        new_message = ''
        for p in paths:
            new_message += p.split('/')[-1] + '\n'
        if new_message != '':
            message['text'] = new_message

    def myclick():
        global paths
        message['text'] = 'Converting imgage(s).'
        convert_images(paths, selection.get())
        paths = []
        message['text'] = 'Finished converting image(s).'

    # Create frame instance
    window = Tk()

    # Set frame geometry
    window.geometry("750x450")

    frame = LabelFrame(window, width=650, height=350, bd=0, background='black')
    frame.grid(column=0, row=0, columnspan=2, rowspan=4, padx=50, pady=50)

    Label(window, text="Python-based image converter", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=0, columnspan=2)

    Label(window, text="Convert images to: ", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=1, sticky=E)
    selection = ttk.Combobox(
        state='readonly',
        values=formats,
    )
    selection.set('.jpg')
    selection.grid(column=1, row=1, sticky=W)

    message = Label(window, text="No files selected", anchor='nw')
    message.grid(column=0, row=2, columnspan=2, sticky='NSEW')

    ttk.Button(window, text = "Select Images", command = pickFiles).grid(column=0, row=3, sticky='NSEW', padx=20, pady=20)

    ttk.Button(window, text="Convert Images =>", command= myclick).grid(column=1, row=3, sticky='NSEW', padx=20, pady=20)
    window.configure(background='black')
    window.mainloop()

if __name__ == "__main__":
    generate_program_window()