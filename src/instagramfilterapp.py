import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

class InstagramFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram-like Filters")

        self.original_image = None
        self.filtered_image = None
        self.filter_intensity = 1.0

        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.filter_options = {
            "Normal": None,
            "Grayscale": ImageFilter.GaussianBlur(2),
            "Blur": ImageFilter.GaussianBlur(5),
            "Sharpness": ImageFilter.SHARPEN,
            "Brightness": "Brightness",
            "Contrast": "Contrast"
        }

        self.filter_var = tk.StringVar()
        self.filter_var.set("Normal")

        self.filter_dropdown = tk.OptionMenu(root, self.filter_var, *self.filter_options.keys())
        self.filter_dropdown.pack()

        self.intensity_label = tk.Label(root, text="Intensity:")
        self.intensity_label.pack()

        self.intensity_scale = tk.Scale(root, from_=0.1, to=2.0, resolution=0.1, orient=tk.HORIZONTAL)
        self.intensity_scale.set(1.0)
        self.intensity_scale.pack()

        self.apply_button = tk.Button(root, text="Apply Filter", command=self.apply_filter)
        self.apply_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.filtered_image = self.original_image.copy()
            self.show_image()

    def show_image(self):
        self.filtered_image.thumbnail((500, 500))
        photo = ImageTk.PhotoImage(self.filtered_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def apply_filter(self):
        selected_filter = self.filter_var.get()
        filter_option = self.filter_options[selected_filter]

        if filter_option is None:
            self.filtered_image = self.original_image.copy()
        elif filter_option == "Brightness":
            self.apply_brightness()
        elif filter_option == "Contrast":
            self.apply_contrast()
        else:
            self.apply_pillow_filter(filter_option)

        self.show_image()

    def apply_brightness(self):
        brightness_factor = self.intensity_scale.get()
        enhancer = ImageEnhance.Brightness(self.original_image)
        self.filtered_image = enhancer.enhance(brightness_factor)

    def apply_contrast(self):
        contrast_factor = self.intensity_scale.get()
        enhancer = ImageEnhance.Contrast(self.original_image)
        self.filtered_image = enhancer.enhance(contrast_factor)

    def apply_pillow_filter(self, filter_option):
        self.filtered_image = self.original_image.filter(filter_option)
        self.apply_intensity()

    def apply_intensity(self):
        intensity = self.intensity_scale.get()
        enhancer = ImageEnhance.Brightness(self.filtered_image)
        self.filtered_image = enhancer.enhance(intensity)

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramFilterApp(root)
    root.mainloop()