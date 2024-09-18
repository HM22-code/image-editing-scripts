import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
import os
from PIL import Image, ImageTk, ImageOps, ImageFilter, ImageDraw, ImageFont
from urllib.request import urlopen

class ImageModel:
    def __init__(self):
        self.image = None

    def load_image(self, path):
        self.image = Image.open(path)
        return self.image

    def load_url(self, url):
        self.image = Image.open(urlopen(url))
        return self.image

    def multiplicate(self):
        """ Multiplicate an image inside herself
        """
        if self.image:
            W,H=self.image.size
            self.image.convert("RGB")
            IT=int(input("Enter number of iterations: "))
            for n in range(0,IT,1):
                for y in range(0,H,1):
                    for x in range(0,W,1):
                        r,g,b=self.image.getpixel((x,y))
                        x2=x//2
                        y2=y//2
                        # Reduce image to half
                        self.image.putpixel((x2,y2),(r,g,b))
                        # Copy reduced image to the right
                        x3=x2+W//2
                        self.image.putpixel((x3,y2),(r,g,b))
                        # Copy of the top side of image reduced to the bottom side
                for j in range(0,H//2,1):
                    for i in range(0,W,1):
                        r,g,b=self.image.getpixel((i,j))
                        self.image.putpixel((i,j+H//2),(r,g,b))
            return self.image

    def invert(self):
        """ Invert Colors of image
        """
        if self.image:
            self.image = ImageOps.invert(self.image)
            return self.image

    def transparency(self):
        """ Remove white pixel and replace it with transparent pixel
        """
        if self.image:
            L,H=self.image.size
            image1=self.image.convert("RGBA")
            image2=Image.new("RGBA",(L,H))
            for x in range (L):
                for y in range (H):
                    p=image1.getpixel((x,y))
                    if (p[0]>250 and p[1]>250 and p[2]>250):
                        a=0
                    else :
                        a=255
                    image2.putpixel((x,y),(p[0],p[1],p[2],a))
            self.image = image2
            return self.image

    def edge_ehance(self):
        """ Ehance edge
        """
        if self.image:
            self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            return self.image

    def emboss(self):
        """ Emboss
        """
        if self.image:
            self.image.convert('RGB')
            self.image = self.image.filter(ImageFilter.EMBOSS)
            return self.image

    def emboss_gif(self):
        """ Emboss each frame of GIF image
        """
        if self.image:
            frames = []
            # Process each frame of GIF image
            number_frames = self.image.n_frames
            for frame in range(number_frames):
                self.image.seek(frame)
                img = self.image.copy()
                img = img.convert('RGB')
                result = img.filter(ImageFilter.EMBOSS)
                frames.append(result)
            frames[0].save('emboss.gif', save_all = True, append_images = frames[1:],  optimize = False)
            return frames[0]

    def pixelate(self):
        """ Pixelate image
        """
        if self.image:
            # Resize smoothly down to 64x64 pixels
            img_small = self.image.resize((64,64), resample=Image.Resampling.BILINEAR)
            # Scale back up using NEAREST to original size
            self.image = img_small.resize(self.image.size, Image.Resampling.NEAREST)
            return self.image

    def pixelate_gif(self):
        """ Pixelate each frame of GIF image
        """
        if self.image:
            frames = []
            # Process each frame of GIF image
            number_frames = self.image.n_frames
            for frame in range(number_frames):
                self.image.seek(frame)
                img = self.image.copy()
                # Resize smoothly down to 128x128 pixels
                img_small = img.resize((128,128), resample=Image.Resampling.BILINEAR)
                # Scale back up using NEAREST to original size
                result = img_small.resize(img.size, Image.Resampling.NEAREST)
                frames.append(result)
            frames[0].save('pixelate.gif', save_all = True, append_images = frames[1:],  optimize = False)
            print("pixelate gif done")
            frames[0].show()

    def extract_img_gif(self):
        """ get png of each frame of GIF image
        """
        if self.image:
            name = str(input("name: "))
            # Process each frame of GIF image
            number_frames = self.image.n_frames
            for frame in range(number_frames):
                self.image.seek(frame)
                img = self.image.copy()
                file = str(name)+"-"+str(frame)+".png"
                img.save(file)

    def apply_comic_filters(self, image):
        # Apply a series of filters to achieve the comic book style
        cartoon_image = image.copy()
        cartoon_image = cartoon_image.convert("L")
        # cartoon_image = cartoon_image.point(lambda p: 255 if p > 128 else 0)
        cartoon_image = cartoon_image.filter(ImageFilter.CONTOUR)
        cartoon_image = cartoon_image.filter(ImageFilter.SMOOTH_MORE)
        return cartoon_image

    def add_text_overlay(self, image, text):
        # Add text overlay to the image
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()  # You can also load custom fonts
        text_position = (20, 20)  # Position of the text overlay
        draw.text(text_position, text, font=font)
        return image

    def comic(self):
        """ Comic image
        """
        if self.image:
            # Apply comic book filters
            self.image = self.apply_comic_filters(self.image)
            return self.image

    def comic_gif(self):
        """ Comic each frame of GIF image
        """
        if self.image:
            frames = []
            # Process each frame of GIF image
            number_frames = self.image.n_frames
            for frame in range(number_frames):
                self.image.seek(frame)
                img = self.image.copy()
                img = img.convert('RGB')
                result = self.apply_comic_filters(img)
                frames.append(result)
            frames[0].save('comic.gif', save_all = True, append_images = frames[1:],  optimize = False)
            frames[0].show()

    def watermarklogo(self):
        if self.image:
            img_logo.show()
            # convert image to black and white (grayscale)
            img_logo = img_logo.convert("L")
            threshold = 50
            img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
            img_logo = img_logo.resize((img_logo.width // 2, img_logo.height // 2))
            img_logo = img_logo.filter(ImageFilter.CONTOUR)
            img_logo.show()
            img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
            img_logo.show()
            self.image.paste(img_logo, (480, 160), img_logo)
            return self.image

    def watermarkbackground(self):
        if self.image:
            self.image.convert("RGB")
            # get image size
            img_width, img_height = self.image.size
            # 5 by 4 water mark grid
            wm_size = (int(img_width * 0.20), int(img_height * 0.25))
            wm_txt = Image.new("RGBA", wm_size, (255, 255, 255, 0))
            # set text size, 1:40 of the image width
            font_size = int(img_width / 40)
            # load font e.g. gotham-bold.ttf
            font = ImageFont.truetype(ImageFont.load_default(), font_size)
            d = ImageDraw.Draw(wm_txt)
            wm_text = "Name"
            # centralize text
            left = (wm_size[0] - font.getsize(wm_text)[0]) / 2
            top = (wm_size[1] - font.getsize(wm_text)[1]) / 2
            # RGBA(0, 0, 0, alpha) is black
            # alpha channel specifies the opacity for a colour
            alpha = 75
            # write text on blank wm_text image
            d.text((left, top), wm_text, fill=(0, 0, 0, alpha), font=font)
            # uncomment to rotate watermark text
            # wm_txt = wm_txt.rotate(15,  expand=1)
            # wm_txt = wm_txt.resize(wm_size, Image.ANTIALIAS)
            for i in range(0, img_width, wm_txt.size[0]):
                for j in range(0, img_height, wm_txt.size[1]):
                    self.image.paste(wm_txt, (i, j), wm_txt)
            # save image with watermark
            self.image.save("watermark.png")
            # show image with watermark in preview
            return self.image

    def watermarktext(self):
        if self.image:
            self.image.convert("RGB")
            # get image size
            img_width, img_height = self.image.size
            # 5 by 4 water mark grid
            wm_size = (int(img_width * 0.20), int(img_height * 0.25))
            wm_txt = Image.new("RGBA", wm_size, (255, 255, 255, 0))
            # set text size, 1:40 of the image width
            font_size = int(img_width / 40)
            # load font e.g. gotham-bold.ttf
            font = ImageFont.truetype(ImageFont.load_default(), font_size)
            d = ImageDraw.Draw(wm_txt)
            wm_text = "Name"
            # centralize text
            left = (wm_size[0] - font.getsize(wm_text)[0]) / 2
            top = (wm_size[1] - font.getsize(wm_text)[1]) / 2
            # RGBA(0, 0, 0, alpha) is black
            # alpha channel specifies the opacity for a colour
            alpha = 75
            # write text on blank wm_text image
            d.text((left, top), wm_text, fill=(0, 0, 0, alpha), font=font)
            # uncomment to rotate watermark text
            # wm_txt = wm_txt.rotate(15,  expand=1)
            # wm_txt = wm_txt.resize(wm_size, Image.ANTIALIAS)
            self.image.paste(wm_txt, (0, 0), wm_txt)
            # save image with watermark
            self.image.save("watermark.png")
            # show image with watermark in preview
            return self.image

    def resize_and_watermark(self, input_folder, output_folder, target_size, watermark_path):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        watermark = Image.open(watermark_path).convert("RGBA")
        for filename in os.listdir(input_folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                img = Image.open(input_path)
                img = img.resize(target_size, Image.ANTIALIAS)
                watermark_position = (img.width - watermark.width, img.height - watermark.height)
                img.paste(watermark, watermark_position, watermark)
                img.save(output_path)

    def thumbnail(self):
        if self.image:
            # set the maximum width and height for the thumbnail
            max_thumbnail_size = (200, 200)
            # applying size for thumbnail
            self.image.thumbnail(max_thumbnail_size)
            # show image in preview
            return self.image

    def convert_to_grayscale(self):
        if self.image:
            self.image = ImageOps.grayscale(self.image)
        return self.image

    def rotate_image(self):
        if self.image:
            self.image = self.image.rotate(90, expand=True)
        return self.image

    def show_image(self):
        if self.image:
            self.image.show()

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)

class ImageView:
    def __init__(self, root):
        self.root = root
        self.root.title("Image editing app")
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
        #self.view.grayscale_button.config(command=self.convert_to_grayscale)
        #self.view.rotate_button.config(command=self.rotate_image)

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

    def open_url(self):
        try:
            url = str(self.url_entry.get())
            image = self.model.load_url(url)
            showinfo(title='Selected File', message=url)
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
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=(('image files', '.png'),('image files', '.jpg'),('image files', '.jpeg'),('image files', '.gif')))
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
                showinfo(title='Selected File', message='Wrong file format selected')
        else:
            showinfo(title='Selected File', message='No file selected.')

    def save_image(self):
        if self.model.image:
            save_path = fd.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                self.model.save_image(save_path)

    def show_image(self):
        if self.model.image:
            self.model.show_image()

class ImageApp:
    def __init__(self):
        root = tk.Tk()
        # Initialize MVC components
        model = ImageModel()
        view = ImageView(root)
        controller = ImageController(model, view)
        root.mainloop()

if __name__ == "__main__":
    ImageApp()