import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
import edit
from PIL import Image, ImageTk
from urllib.request import urlopen


class ImageEditorApp:
    # TODO : MVC
    def __init__(self, root):
        self.filename = None
        self.image = None
        self.preview = None
        self.root = root
        self.root.title("Image editing scripts")
        self.root.iconbitmap("assets/favicon.ico")
        self.root.resizable(False, False)
        self.root.geometry("500x700")
        self.root.eval("tk::PlaceWindow . center")
        self.root.config(bg="#f0f0f0")

        self.pack_widgets()

    def pack_widgets(self):
        """ Init widgets
        """
        # Create UI components
        self.canvas = tk.Canvas(self.root, width=200, height=200)
        self.canvas.pack()

        # File frame
        self.file_frame = tk.Frame(self.root)
        self.file_frame.pack(pady=10)

        # Open image file
        open_button = ttk.Button(self.file_frame, text='Open File', command=self.select_files)
        open_button.grid(row=0, column=0, padx=10, pady=5)

        # Save Button
        self.save_button = ttk.Button(self.file_frame, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.grid(row=0, column=1, padx=10, pady=5)

        # URL Input and Button
        self.url_frame = tk.Frame(self.root)
        self.url_frame.pack(pady=10)

        self.url_label = ttk.Label(self.url_frame, text="Image URL:")
        self.url_label.pack(side=tk.LEFT, padx=10)

        self.url_entry = ttk.Entry(self.url_frame, width=30, font=("Arial", 12))
        self.url_entry.pack(side=tk.LEFT, padx=10)

        self.load_url_button = ttk.Button(self.url_frame, text='Load from URL', command=self.open_url)
        self.load_url_button.pack(side=tk.LEFT, padx=10)

        # Frame for buttons
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.multiplicate_button = ttk.Button(self.button_frame, text='Multiplicate', command= lambda: edit.multiplicate(self.image), state=tk.DISABLED)
        self.multiplicate_button.grid(row=0, column=0, padx=10, pady=5)

        self.invert_button = ttk.Button(self.button_frame, text='Invert', command= lambda: edit.invert(self.image), state=tk.DISABLED)
        self.invert_button.grid(row=0, column=1, padx=10, pady=5)

        self.transparency_button = ttk.Button(self.button_frame, text='Transparency', command= lambda: edit.transparency(self.image), state=tk.DISABLED)
        self.transparency_button.grid(row=1, column=0, padx=10, pady=5)

        self.edge_ehance_button = ttk.Button(self.button_frame, text='Edge Ehance', command= lambda: edit.edge_ehance(self.image), state=tk.DISABLED)
        self.edge_ehance_button.grid(row=1, column=1, padx=10, pady=5)

        self.emboss_button = ttk.Button(self.button_frame, text='Emboss', command= lambda: edit.emboss(self.image), state=tk.DISABLED)
        self.emboss_button.grid(row=2, column=0, padx=10, pady=5)

        self.pixelate_button = ttk.Button(self.button_frame, text='Pixelate', command= lambda: edit.pixelate(self.image), state=tk.DISABLED)
        self.pixelate_button.grid(row=2, column=1, padx=10, pady=5)

        self.comic_button = ttk.Button(self.button_frame, text='Comic', command= lambda: edit.comic(self.image), state=tk.DISABLED)
        self.comic_button.grid(row=3, column=0, padx=10, pady=5)

        self.segmented_button = ttk.Button(self.button_frame, text='Segmented', command= lambda: edit.segmented(self.image), state=tk.DISABLED)
        self.segmented_button.grid(row=3, column=1, padx=10, pady=5)

        # Frame for buttons
        self.gif_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.gif_frame.pack(pady=10)

        self.emboss_gif_button = ttk.Button(self.gif_frame, text='Emboss_GIF', command= lambda: edit.emboss_gif(self.image), state=tk.DISABLED)
        self.emboss_gif_button.grid(row=0, column=0, padx=10, pady=5)

        self.pixelate_gif_button = ttk.Button(self.gif_frame, text='Pixelate_GIF', command= lambda: edit.pixelate_gif(self.image), state=tk.DISABLED)
        self.pixelate_gif_button.grid(row=0, column=1, padx=10, pady=5)

        self.comic_gif_button = ttk.Button(self.gif_frame, text='Comic_GIF', command= lambda: edit.comic_gif(self.image), state=tk.DISABLED)
        self.comic_gif_button.grid(row=1, column=0, padx=10, pady=5)

        self.extract_img_gif_button = ttk.Button(self.gif_frame, text='Extract_GIF', command= lambda: edit.extract_img_gif(self.image), state=tk.DISABLED)
        self.extract_img_gif_button.grid(row=1, column=1, padx=10, pady=5)

    def set_buttons_state(self, state):
        self.multiplicate_button.config(state=state)
        self.invert_button.config(state=state)
        self.transparency_button.config(state=state)
        self.edge_ehance_button.config(state=state)
        self.emboss_button.config(state=state)
        self.pixelate_button.config(state=state)
        self.comic_button.config(state=state)
        self.segmented_button.config(state=state)

    def set_gif_state(self, state):
        self.emboss_gif_button.config(state=state)
        self.pixelate_gif_button.config(state=state)
        self.comic_gif_button.config(state=state)
        self.extract_img_gif_button.config(state=state)

    def update_preview(self):
        self.preview.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(self.preview)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def open_url(self):
        try:
            url = str(self.url_entry.get())
            self.image = Image.open(urlopen(url))
            self.preview = self.image.copy()
            showinfo(title='Selected File', message=url)
            self.update_preview()
            self.save_button.config(state=tk.NORMAL)
            if url.endswith((".png", ".jpg", ".jpeg")):
                self.set_buttons_state(tk.NORMAL)
                self.set_gif_state(tk.DISABLED)
            elif url.endswith(".gif"):
                self.set_gif_state(tk.NORMAL)
                self.set_buttons_state(tk.DISABLED)
        except Exception as e:
            mb.showerror("Error", f"{e}")

    def select_files(self):
        """ Open file dialog and show selected file
        """
        filetypes = (
            ('image files', '.png'),
            ('image files', '.jpg'),
            ('image files', '.jpeg'),
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
            self.update_preview()
            self.save_button.config(state=tk.NORMAL)
            print(self.image.filename)
            print(self.image.size)
            if self.filename.endswith((".png", ".jpg", ".jpeg")):
                self.set_buttons_state(tk.NORMAL)
                self.set_gif_state(tk.DISABLED)
            elif self.filename.endswith(".gif"):
                print(self.image.is_animated)
                print(self.image.n_frames)
                self.set_gif_state(tk.NORMAL)
                self.set_buttons_state(tk.DISABLED)
            else:
                showinfo(title='Selected File', message='Wrong file format selected')
        else:
            showinfo(title='Selected File', message='No file selected.')

    def save_image(self):
        if self.image:
            save_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.image.save(save_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()