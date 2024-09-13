import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import edit
import config
from PIL import Image, ImageTk

class Window:
    def __init__(self):
        self.filename = None
        self.image = None
        self.preview = None
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
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        open_button = ttk.Button(self.root, text='Open a File', command=self.select_files)
        open_button.pack(expand=True)
        multiplicate_button = ttk.Button(self.root, text='Multiplicate', command= lambda: edit.multiplicate(self.image))
        multiplicate_button.pack(expand=True)
        invert_button = ttk.Button(self.root, text='Invert', command= lambda: edit.invert(self.image))
        invert_button.pack(expand=True)
        transparency_button = ttk.Button(self.root, text='Transparency', command= lambda: edit.transparency(self.image))
        transparency_button.pack(expand=True)
        edge_ehance_button = ttk.Button(self.root, text='Edge Ehance', command= lambda: edit.edge_ehance(self.image))
        edge_ehance_button.pack(expand=True)
        emboss_button = ttk.Button(self.root, text='Emboss', command= lambda: edit.emboss(self.image))
        emboss_button.pack(expand=True)
        emboss_gif_button = ttk.Button(self.root, text='Emboss_GIF', command= lambda: edit.emboss_gif(self.image))
        emboss_gif_button.pack(expand=True)
        pixelate_button = ttk.Button(self.root, text='Pixelate', command= lambda: edit.pixelate(self.image))
        pixelate_button.pack(expand=True)
        pixelate_gif_button = ttk.Button(self.root, text='Pixelate_GIF', command= lambda: edit.pixelate_gif(self.image))
        pixelate_gif_button.pack(expand=True)
        extract_img_gif_button = ttk.Button(self.root, text='Extract_GIF', command= lambda: edit.extract_img_gif(self.image))
        extract_img_gif_button.pack(expand=True)
        comic_button = ttk.Button(self.root, text='Comic', command= lambda: edit.comic(self.image))
        comic_button.pack(expand=True)
        comic_gif_button = ttk.Button(self.root, text='Comic_GIF', command= lambda: edit.comic_gif(self.image))
        comic_gif_button.pack(expand=True)
        segmented_button = ttk.Button(self.root, text='Segmented', command= lambda: edit.segmented(self.image))
        segmented_button.pack(expand=True)

    def show_image(self):
        self.preview.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(self.preview)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

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
            ('image files', '.gif'),
        )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        if self.filename:
            self.image = Image.open(self.filename)
            self.preview = self.image.copy()
            showinfo(title='Selected File', message=self.filename)
            self.show_image()
        else:
            showinfo(title='Selected File', message='No file selected.')