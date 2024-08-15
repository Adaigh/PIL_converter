from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames

formats = ['.jpg', '.jpeg', '.png', '.bmp', '.blp', '.dds', '.dib', '.eps', '.gif', '.icns', '.ico', '.im', '.msp', '.pcx', '.pfm', '.ppm', '.tga', '.tiff', '.webp']
d_font = font=('Arial', 20, "bold")

def generate_program_window():

    paths = []

    def pickFiles():
        paths = [file for file in askopenfilenames()]
        new_message = ''
        for p in paths:
            new_message += p.split('/')[-1] + '\n'
        message['text'] = new_message
        message['font'] = ('Arial', 12)

    def myclick():
        message = "Hello, " + entry.get()
        label = Label(frame, text = message, font = ("Times New Roman", 14, "italic"))
        entry.delete(0,'end')
        label.pack(pady=30)

    # Create frame instance
    window = Tk()

    # Set frame geometry
    window.geometry("750x750")

    frame = LabelFrame(window, width=650, height=650, bd=0, background='black').grid(column=0, row=0, columnspan=2, rowspan=4, padx=50, pady=50)

    Label(frame, text="Python-based image converter", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=0, columnspan=2)
    message = Label(frame, text="No files selected", font=d_font, background='black', foreground='#5bb963')
    message.grid(column=0, row=1)
    ttk.Button(frame, text = "Select Images", command = pickFiles).grid(column=1, row=1)
    Label(frame, text="Convert images to: ", font=d_font, background='black', foreground='#5bb963').grid(column=0, row=2)
    ttk.Combobox(
        state='readonly',
        values=formats,
        font=d_font,
        background='black',
        foreground='#5bb963'
    ).grid(column=1, row=2)

    ttk.Button(frame, text="Click", command= myclick).grid(column=0, row=3, columnspan=2, pady=20)
    window.configure(background='black')
    window.mainloop()

if __name__ == "__main__":
    generate_program_window()