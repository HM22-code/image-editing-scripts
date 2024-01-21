import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageFilter
import PIL.ImageOps 

class main:

    def __init__(self):
        self.filename = None

    def select_file(self):
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
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=self.filename
        )

        
    def multiplicate(self):
        """ Multiplicate an image inside herself
        """
        photo=Image.open(self.filename)
        # Get image size
        L,H=photo.size
        iterations=int(input("Enter number of iterations: "))
        for n in range(0,iterations,1):
            for y in range(0,H,1):
                for x in range(0,L,1):
                    r,v,b=photo.getpixel((x,y))
                    x2=x//2
                    y2=y//2
                    # Reduce image to half
                    photo.putpixel((x2,y2),(r,v,b))
                    # Copy reduced image to the right
                    x3=x2+L//2
                    photo.putpixel((x3,y2),(r,v,b))
                    # Copy of the top side of image reduced to the bottom side
            for j in range(0,H//2,1):
                for i in range(0,L,1):
                    ro,ve,bl=photo.getpixel((i,j))
                    photo.putpixel((i,j+H//2),(ro,ve,bl))
        print("iterations: ",n+1)
        photo.show()

    def invert(self):
        """ Invert Colors of image
        """
        image=Image.open(self.filename)
        image2 = PIL.ImageOps.invert(image)
        image2.show()

    def transparancy(self):
        """ Remove white pixel and replace it with transparent pixel
        """
        image=Image.open(self.filename)
        L,H=image.size
        image1=image.convert("RGBA")
        image2=Image.new("RGBA",(L,H))
        for x in range (L):
            for y in range (H):
                p=image1.getpixel((x,y))
                if (p[0]>250 and p[1]>250 and p[2]>250):
                    a=0
                else :
                    a=255
                image2.putpixel((x,y),(p[0],p[1],p[2],a))
        #image2.save("filename.png")
        image2.show()

    def edge_ehance(self):
        """ Ehance edge
        """
        image=Image.open(self.filename)
        image2 = image.filter(ImageFilter.EDGE_ENHANCE)
        image2.show()
        
    def pixelate(self):
        """ Pixelate image
        """
        # Open image
        img = Image.open(self.filename)
        # Resize smoothly down to 64x64 pixels
        img_small = img.resize((64,64), resample=Image.Resampling.BILINEAR)
        # Scale back up using NEAREST to original size
        result = img_small.resize(img.size, Image.Resampling.NEAREST)
        result.show()
    
    def pixelate_gif(self):
        """ Pixelate each frame of GIF image
        """
        images = []
        gif = Image.open(self.filename)
        # Process each frame of GIF image
        number_frames = gif.n_frames
        for frame in range(number_frames):
            gif.seek(frame)
            img = gif.copy()
            # Resize smoothly down to 128x128 pixels
            img_small = img.resize((128,128), resample=Image.Resampling.BILINEAR)
            # Scale back up using NEAREST to original size
            result = img_small.resize(img.size, Image.Resampling.NEAREST)
            images.append(result)
        images[0].save('pillow.gif', save_all = True, append_images = images[1:],  optimize = False)
        print("GIF created")

    def run(self):
        """ Main function
        """
        # create the root window
        root = tk.Tk()
        root.title('Image editing scripts')
        root.iconbitmap("hm.ico")
        root.resizable(False, False)
        root.geometry('300x300')
        root.eval('tk::PlaceWindow . center')
        # open button
        open_button = ttk.Button(
            root,
            text='Open a File',
            command=self.select_file
        )
        # multiplicate button
        multiplicate_button = ttk.Button(
            root,
            text='Multiplicate',
            command=self.multiplicate
        )
        # invert button
        invert_button = ttk.Button(
            root,
            text='Invert',
            command=self.invert
        )
        # transparency button
        transparency_button = ttk.Button(
            root,
            text='Transparancy',
            command=self.transparancy
        )
        # edge ehance button
        edge_ehance_button = ttk.Button(
            root,
            text='Edge Ehance',
            command=self.edge_ehance
        )
        # pixelate button
        pixelate_button = ttk.Button(
            root,
            text='Pixelate',
            command=self.pixelate
        )
        # pixelate gif button
        pixelate_gif_button = ttk.Button(
            root,
            text='Pixelate_GIF',
            command=self.pixelate_gif
        )
        # pack widgets
        open_button.pack(expand=True)
        multiplicate_button.pack(expand=True)
        invert_button.pack(expand=True)
        transparency_button.pack(expand=True)
        edge_ehance_button.pack(expand=True)
        pixelate_button.pack(expand=True)
        pixelate_gif_button.pack(expand=True)
        # run the application
        root.mainloop()

if __name__ == '__main__':
    main().run()



