import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import os

class Window:
    def __init__(self):
        self.filename = None
        self.original_image = None
        self.filtered_image = None
        self.root = tk.Tk()
        self.root.title("Convert webp")
        self.root.iconbitmap("assets/favicon.ico")
        self.root.resizable(False, False)
        self.root.geometry("600x600")
        self.root.eval("tk::PlaceWindow . center")
        self.pack_widgets()

    def pack_widgets(self):
        """ Init widgets
        """
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        open_button = ttk.Button(self.root, text='Open a File', command=self.select_files)
        open_button.pack(expand=True)
        convert_button = ttk.Button(self.root, text='Convert', command=self.convert_webp)
        convert_button.pack(expand=True)
        # Filter frame
        self.filter_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.filter_frame.pack(pady=10)
        self.filter_options = {
            "png": "png",
            "gif": "gif",
        }
        self.filter_var = tk.StringVar()
        # Filter dropdown
        self.filter_dropdown = ttk.OptionMenu(self.filter_frame, self.filter_var, *self.filter_options.keys())
        self.filter_dropdown.grid(row=0, column=0, padx=10, pady=5)

    def update_preview(self):
        self.filtered_image.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(self.filtered_image)
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
            ('image files', '.webp'),
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

    def convert_webp(self):
        """
        Convert a .webp image file to either .png or .gif format.

        Args:
            input_file (str): Path to the input .webp file.
            output_format (str): Output format, either 'png' or 'gif'.
        """
        # Get image output format
        selected_filter = self.filter_var.get()
        output_format = self.filter_options[selected_filter]
        input_file = self.filename
        # Check if the input file is a .webp file
        if not input_file.lower().endswith('.webp'):
            print(f"Error: The file {input_file} is not a .webp file.")
            return
        # Load the webp image
        try:
            with Image.open(input_file) as img:
                # Determine the output file name
                output_file = os.path.splitext(input_file)[0] + f'.{output_format}'
                if output_format == "gif":
                    img.info.pop('background', None)
                    img.save(output_file, 'gif', save_all=True)
                    print(f"Image successfully converted to {output_file}")
                elif output_format == "png":
                    img.save(output_file, format=output_format.upper())
                    print(f"Image successfully converted to {output_file}")
        except Exception as e:
            print(f"Error: {e}")

Window().run()