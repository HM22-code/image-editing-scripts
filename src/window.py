import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import edit
import config

class Window:
    def __init__(self):
        self.filename = None
        self.root = tk.Tk()
        self.root.title(config.TITLE)
        self.root.iconbitmap(config.ICONBITMAP)
        self.root.resizable(False, False)
        self.root.geometry(config.GEOMETRY)
        self.root.eval(config.EVAL)
        self.pack_widgets()

    def pack_widgets(self):
        """ Init widgets
        """
        open_button = ttk.Button(self.root, text='Open a File', command=self.select_files)
        multiplicate_button = ttk.Button(self.root, text='Multiplicate', command= lambda: edit.multiplicate(self.filename))
        invert_button = ttk.Button(self.root, text='Invert', command= lambda: edit.invert(self.filename))
        transparency_button = ttk.Button(self.root, text='Transparency', command= lambda: edit.transparency(self.filename))
        edge_ehance_button = ttk.Button(self.root, text='Edge Ehance', command= lambda: edit.edge_ehance(self.filename))
        emboss_button = ttk.Button(self.root, text='Emboss', command= lambda: edit.emboss(self.filename))
        emboss_gif_button = ttk.Button(self.root, text='Emboss_GIF', command= lambda: edit.emboss_gif(self.filename))
        pixelate_button = ttk.Button(self.root, text='Pixelate', command= lambda: edit.pixelate(self.filename))
        pixelate_gif_button = ttk.Button(self.root, text='Pixelate_GIF', command= lambda: edit.pixelate_gif(self.filename))
        extract_img_gif_button = ttk.Button(self.root, text='Extract_img_GIF', command= lambda: edit.extract_img_gif(self.filename))
        comic_button = ttk.Button(self.root, text='Comic', command= lambda: edit.comic(self.filename))
        open_button.pack(expand=True)
        multiplicate_button.pack(expand=True)
        invert_button.pack(expand=True)
        transparency_button.pack(expand=True)
        edge_ehance_button.pack(expand=True)
        emboss_button.pack(expand=True)
        emboss_gif_button.pack(expand=True)
        pixelate_button.pack(expand=True)
        pixelate_gif_button.pack(expand=True)
        extract_img_gif_button.pack(expand=True)
        comic_button.pack(expand=True)

    def run(self):
        """ Run the window
        """
        self.root.mainloop()

    def select_files(self):
        """ Open file dialog and show selected file
        """
        filetypes = (
            ('image files', '.png'),
            ('image files', '.jpg'),
            ('GIF image files', '.gif'),
        )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        showinfo(
            title='Selected File',
            message=self.filename
        )