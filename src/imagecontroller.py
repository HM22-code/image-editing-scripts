import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo

class ImageController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Connect buttons to actions
        self.view.open_button.config(command=self.select_files)
        self.view.save_button.config(command=self.save_image)
        self.view.show_button.config(command=self.show_image)
        self.view.load_url_button.config(command=self.open_url)
        self.view.multiplicate_button.config(command=self.multiplicate)
        self.view.invert_button.config(command=self.invert)
        self.view.transparency_button.config(command=self.transparency)
        self.view.edge_ehance_button.config(command=self.edge_ehance)
        self.view.emboss_button.config(command=self.emboss)
        self.view.pixelate_button.config(command=self.pixelate)
        self.view.comic_button.config(command=self.comic)
        self.view.emboss_gif_button.config(command=self.emboss_gif)
        self.view.pixelate_gif_button.config(command=self.pixelate_gif)
        self.view.comic_gif_button.config(command=self.comic_gif)
        self.view.apply_button.config(command=self.apply_filter)

    def multiplicate(self):
        image = self.model.multiplicate()
        if image:
            self.view.update_preview(image)

    def invert(self):
        image = self.model.invert()
        if image:
            self.view.update_preview(image)

    def transparency(self):
        image = self.model.transparency()
        if image:
            self.view.update_preview(image)

    def edge_ehance(self):
        image = self.model.edge_ehance()
        if image:
            self.view.update_preview(image)

    def emboss(self):
        image = self.model.emboss()
        if image:
            self.view.update_preview(image)

    def emboss_gif(self):
        image = self.model.emboss_gif()
        if image:
            self.view.update_preview(image)

    def pixelate(self):
        image = self.model.pixelate()
        if image:
            self.view.update_preview(image)

    def pixelate_gif(self):
        image = self.model.pixelate_gif()
        if image:
            self.view.update_preview(image)

    def extract_img_gif(self):
        image = self.model.extract_img_gif()
        if image:
            self.view.update_preview(image)

    def comic(self):
        image = self.model.comic()
        if image:
            self.view.update_preview(image)

    def comic_gif(self):
        image = self.model.comic_gif()
        if image:
            self.view.update_preview(image)

    def watermarklogo(self):
        image = self.model.watermarklogo()
        if image:
            self.view.update_preview(image)

    def watermarkbackground(self):
        image = self.model.watermarkbackground()
        if image:
            self.view.update_preview(image)

    def watermarktext(self):
        image = self.model.watermarktext()
        if image:
            self.view.update_preview(image)

    def resize_and_watermark(self, input_folder, output_folder, target_size, watermark_path):
        image = self.model.resize_and_watermark(input_folder, output_folder, target_size, watermark_path)
        if image:
            self.view.update_preview(image)

    def thumbnail(self):
        image = self.model.thumbnail()
        if image:
            self.view.update_preview(image)

    def convert_to_grayscale(self):
        image = self.model.convert_to_grayscale()
        if image:
            self.view.update_preview(image)

    def rotate_image(self):
        image = self.model.rotate_image()
        if image:
            self.view.update_preview(image)

    def apply_filter(self):
        selected_filter = self.view.filter_var.get()
        filter_option = self.view.filter_options[selected_filter]
        intensity_scale = self.view.intensity_scale.get()
        image = self.model.apply_filter(filter_option, intensity_scale)
        if image:
            self.view.update_preview(image)

    def open_url(self):
        try:
            url = str(self.url_entry.get())
            image = self.model.load_url(url)
            showinfo(title='Selected URL File', message=url)
            self.view.update_preview(image)
            self.view.save_button.config(state=tk.NORMAL)
            self.view.show_button.config(state=tk.NORMAL)
            if url.endswith((".png", ".jpg", ".jpeg")):
                self.view.set_buttons_state(tk.NORMAL)
                self.view.set_gif_state(tk.DISABLED)
            elif url.endswith(".gif"):
                self.view.set_gif_state(tk.NORMAL)
                self.view.set_buttons_state(tk.DISABLED)
        except Exception as e:
            mb.showerror("Error", f"{e}")

    def select_files(self):
        """ Open file dialog and show selected file
        """
        typename = 'image files'
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=((typename, '.png'),(typename, '.jpg'),(typename, '.jpeg'),(typename, '.gif')))
        if filename:
            image = self.model.load_image(filename)
            showinfo(title='Selected File', message=filename)
            self.view.update_preview(image)
            self.view.save_button.config(state=tk.NORMAL)
            self.view.show_button.config(state=tk.NORMAL)
            if filename.endswith((".png", ".jpg", ".jpeg")):
                self.view.set_buttons_state(tk.NORMAL)
                self.view.set_gif_state(tk.DISABLED)
            elif filename.endswith(".gif"):
                self.view.set_gif_state(tk.NORMAL)
                self.view.set_buttons_state(tk.DISABLED)
            else:
                showinfo(title='Info', message='Wrong file format selected')
        else:
            showinfo(title='Info', message='No file selected.')

    def save_image(self):
        if self.model.image:
            save_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.model.save_image(save_path)
                showinfo(title='Info', message='Image saved.')

    def show_image(self):
        if self.model.image:
            self.model.show_image()