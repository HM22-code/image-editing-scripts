import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk, ImageFilter
import PIL.ImageOps

class Window:
    def __init__(self):
        self.filename = None
        self.original_image = None
        self.filtered_image = None
        self.root = tk.Tk()
        self.root.title("Edge Detect")
        self.root.iconbitmap("assets/favicon.ico")
        self.root.resizable(False, False)
        self.root.geometry("800x800")
        self.root.eval("tk::PlaceWindow . center")
        self.pack_widgets()

    def pack_widgets(self):
        """ Init widgets
        """
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        open_button = ttk.Button(self.root, text='Open a File', command=self.select_files)
        open_button.pack(expand=True)
        edge_detect_button = ttk.Button(self.root, text='Edge Detect', command=self.edge_detect)
        edge_detect_button.pack(expand=True)
        convert_button = ttk.Button(self.root, text='Convert', command=self.convert)
        convert_button.pack(expand=True)
        invert_button = ttk.Button(self.root, text='Invert', command=self.invert)
        invert_button.pack(expand=True)
        save_button = ttk.Button(self.root, text='Save', command=self.save_image)
        save_button.pack(expand=True)
        show_button = ttk.Button(self.root, text='Show', command=self.show_image)
        show_button.pack(expand=True)

    def update_preview(self):
        preview = self.filtered_image.copy()
        preview.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(preview)
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
            ('image files', '.jpeg'),
        )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        if self.filename:
            self.original_image = Image.open(self.filename)
            self.filtered_image = self.original_image.copy()
            showinfo(title='Selected File', message=self.filename)
            self.update_preview()
        else:
            showinfo(title='Selected File', message='No file selected.')

    def edge_detect(self):
        self.filtered_image = self.filtered_image.filter(ImageFilter.FIND_EDGES)
        self.update_preview()

    def convert(self):
        self.filtered_image = self.filtered_image.convert("L")
        self.update_preview()

    def invert(self):
        self.filtered_image = PIL.ImageOps.invert(self.filtered_image)
        self.update_preview()

    def save_image(self):
        if self.filtered_image:
            save_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.filtered_image.save(save_path)
                showinfo(title='Info', message='Image saved.')

    def show_image(self):
        if self.filtered_image:
            self.filtered_image.show()

Window().run()