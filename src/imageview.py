import tkinter as tk
from tkinter import ttk
from PIL import ImageTk

class ImageView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image editing app")
        self.root.iconbitmap("assets/favicon.ico")
        self.root.resizable(False, False)
        self.root.geometry("600x700")
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
        # Open image file button
        self.open_button = ttk.Button(self.file_frame, text='Open File')
        self.open_button.grid(row=0, column=0, padx=10, pady=5)
        # Save image file button
        self.save_button = ttk.Button(self.file_frame, text="Save Image", state=tk.DISABLED)
        self.save_button.grid(row=0, column=1, padx=10, pady=5)
        # Show image file button
        self.show_button = ttk.Button(self.file_frame, text="Show Image", state=tk.DISABLED)
        self.show_button.grid(row=0, column=2, padx=10, pady=5)

        # URL frame
        self.url_frame = tk.Frame(self.root)
        self.url_frame.pack(pady=10)
        # URL Label
        self.url_label = ttk.Label(self.url_frame, text="Image URL:")
        self.url_label.pack(side=tk.LEFT, padx=10)
        # URL entry
        self.url_entry = ttk.Entry(self.url_frame, width=30, font=("Arial", 12))
        self.url_entry.pack(side=tk.LEFT, padx=10)
        # URL load button
        self.load_url_button = ttk.Button(self.url_frame, text='Load from URL')
        self.load_url_button.pack(side=tk.LEFT, padx=10)

        # Filter frame
        self.filter_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.filter_frame.pack(pady=10)
        self.filter_options = {
            "Normal": "Normal",
            "Blur": "Blur",
            "Sharpness": "Sharpness",
            "Brightness": "Brightness",
            "Contrast": "Contrast"
        }
        self.filter_var = tk.StringVar()
        self.filter_var.set("Normal")
        # Filter dropdown
        self.filter_dropdown = ttk.OptionMenu(self.filter_frame, self.filter_var, *self.filter_options.keys())
        self.filter_dropdown.grid(row=0, column=0, padx=10, pady=5)
        # Intensity label
        self.intensity_label = ttk.Label(self.filter_frame, text="Intensity:")
        self.intensity_label.grid(row=0, column=1, padx=10, pady=5)
        # Intensity scale
        self.intensity_scale = ttk.Scale(self.filter_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL)
        self.intensity_scale.set(1.0)
        self.intensity_scale.grid(row=0, column=2, padx=10, pady=5)
        # Apply filter
        self.apply_button = ttk.Button(self.filter_frame, text="Apply Filter", state=tk.DISABLED)
        self.apply_button.grid(row=0, column=3, padx=10, pady=5)

        # Frame for buttons
        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)
        # Multiplicate
        self.multiplicate_button = ttk.Button(self.button_frame, text='Multiplicate', state=tk.DISABLED)
        self.multiplicate_button.grid(row=0, column=0, padx=10, pady=5)
        # Invert
        self.invert_button = ttk.Button(self.button_frame, text='Invert', state=tk.DISABLED)
        self.invert_button.grid(row=0, column=1, padx=10, pady=5)
        # Transparency
        self.transparency_button = ttk.Button(self.button_frame, text='Transparency', state=tk.DISABLED)
        self.transparency_button.grid(row=1, column=0, padx=10, pady=5)
        # Edge ehance
        self.edge_ehance_button = ttk.Button(self.button_frame, text='Edge Ehance', state=tk.DISABLED)
        self.edge_ehance_button.grid(row=1, column=1, padx=10, pady=5)
        # Emboss
        self.emboss_button = ttk.Button(self.button_frame, text='Emboss', state=tk.DISABLED)
        self.emboss_button.grid(row=2, column=0, padx=10, pady=5)
        # Pixelate
        self.pixelate_button = ttk.Button(self.button_frame, text='Pixelate', state=tk.DISABLED)
        self.pixelate_button.grid(row=2, column=1, padx=10, pady=5)
        # Comic
        self.comic_button = ttk.Button(self.button_frame, text='Comic', state=tk.DISABLED)
        self.comic_button.grid(row=3, column=0, padx=10, pady=5)

        # Frame for buttons
        self.gif_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.gif_frame.pack(pady=10)
        # Emboss
        self.emboss_gif_button = ttk.Button(self.gif_frame, text='Emboss_GIF', state=tk.DISABLED)
        self.emboss_gif_button.grid(row=0, column=0, padx=10, pady=5)
        # Pixelate
        self.pixelate_gif_button = ttk.Button(self.gif_frame, text='Pixelate_GIF', state=tk.DISABLED)
        self.pixelate_gif_button.grid(row=0, column=1, padx=10, pady=5)
        # Comic
        self.comic_gif_button = ttk.Button(self.gif_frame, text='Comic_GIF', state=tk.DISABLED)
        self.comic_gif_button.grid(row=1, column=0, padx=10, pady=5)
        # Extract img from GIF
        self.extract_img_gif_button = ttk.Button(self.gif_frame, text='Extract_GIF', state=tk.DISABLED)
        self.extract_img_gif_button.grid(row=1, column=1, padx=10, pady=5)

    def set_buttons_state(self, state):
        self.multiplicate_button.config(state=state)
        self.invert_button.config(state=state)
        self.transparency_button.config(state=state)
        self.edge_ehance_button.config(state=state)
        self.emboss_button.config(state=state)
        self.pixelate_button.config(state=state)
        self.comic_button.config(state=state)
        self.apply_button.config(state=state)

    def set_gif_state(self, state):
        self.emboss_gif_button.config(state=state)
        self.pixelate_gif_button.config(state=state)
        self.comic_gif_button.config(state=state)
        self.extract_img_gif_button.config(state=state)

    def update_preview(self, img):
        self.preview = img.copy()
        self.preview.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(self.preview)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo