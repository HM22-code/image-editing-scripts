from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
import PIL.ImageOps
from urllib.request import urlopen
import os


class ImageModel:
    def __init__(self):
        self.image = None
        self.copy = None

    def load_image(self, path):
        self.image = Image.open(path)
        self.copy = self.image.copy()
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
            self.image.convert("RGB")
            self.image = PIL.ImageOps.invert(self.image)
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

    def apply_filter(self, filter_option, intensity_scale):
        if self.image:
            if filter_option == "Normal":
                self.image = self.copy
            elif filter_option == "Brightness":
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(intensity_scale)
            elif filter_option == "Contrast":
                enhancer = ImageEnhance.Contrast(self.image)
                self.image = enhancer.enhance(intensity_scale)
            elif filter_option == "Blur":
                self.image = self.image.filter(ImageFilter.GaussianBlur(intensity_scale))
            elif filter_option == "Sharpness":
                self.image = self.image.filter(ImageFilter.SHARPEN)
            return self.image

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
            self.image = PIL.ImageOps.grayscale(self.image)
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