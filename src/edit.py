import string
from PIL import Image, ImageFilter
import PIL.ImageOps

def multiplicate(filename):
    """ Multiplicate an image inside herself
    """
    img=Image.open(filename)
    W,H=img.size
    IT=int(input("Enter number of iterations: "))
    for n in range(0,IT,1):
        for y in range(0,H,1):
            for x in range(0,W,1):
                r,g,b=img.getpixel((x,y))
                x2=x//2
                y2=y//2
                # Reduce image to half
                img.putpixel((x2,y2),(r,g,b))
                # Copy reduced image to the right
                x3=x2+W//2
                img.putpixel((x3,y2),(r,g,b))
                # Copy of the top side of image reduced to the bottom side
        for j in range(0,H//2,1):
            for i in range(0,W,1):
                r,g,b=img.getpixel((i,j))
                img.putpixel((i,j+H//2),(r,g,b))
    img.save("multiplicate-" + str(n) + ".png")
    print("multiplicate done")
    img.show()

def invert(filename):
    """ Invert Colors of image
    """
    image=Image.open(filename)
    image2 = PIL.ImageOps.invert(image)
    image2.save("invert.png")
    print("invert done")
    image2.show()

def transparency(filename):
    """ Remove white pixel and replace it with transparent pixel
    """
    image=Image.open(filename)
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
    image2.save("transparency.png")
    print("transparency done")
    image2.show()

def edge_ehance(filename):
    """ Ehance edge
    """
    image=Image.open(filename)
    image2 = image.filter(ImageFilter.EDGE_ENHANCE)
    image2.save("edge_ehance.png")
    print("edge ehance done")
    image2.show()

def emboss(filename):
    """ Emboss
    """
    image=Image.open(filename)
    image2 = image.filter(ImageFilter.EMBOSS)
    image2.save("emboss.png")
    print("emboss done")

def pixelate(filename):
    """ Pixelate image
    """
    # Open image
    img = Image.open(filename)
    # Resize smoothly down to 64x64 pixels
    img_small = img.resize((64,64), resample=Image.Resampling.BILINEAR)
    # Scale back up using NEAREST to original size
    result = img_small.resize(img.size, Image.Resampling.NEAREST)
    result.save("pixelate.png")
    print("pixelate done")
    result.show()

def pixelate_gif(filename):
    """ Pixelate each frame of GIF image
    """
    frames = []
    gif = Image.open(filename)
    # Process each frame of GIF image
    number_frames = gif.n_frames
    for frame in range(number_frames):
        gif.seek(frame)
        img = gif.copy()
        # Resize smoothly down to 128x128 pixels
        img_small = img.resize((128,128), resample=Image.Resampling.BILINEAR)
        # Scale back up using NEAREST to original size
        result = img_small.resize(img.size, Image.Resampling.NEAREST)
        frames.append(result)
    frames[0].save('pixelate.gif', save_all = True, append_images = frames[1:],  optimize = False)
    print("pixelate gif done")
    frames[0].show()

def extract_img_gif(filename):
    """ get png of each frame of GIF image
    """
    gif = Image.open(filename)
    name = str(input("name: "))
    # Process each frame of GIF image
    number_frames = gif.n_frames
    for frame in range(number_frames):
        gif.seek(frame)
        img = gif.copy()
        file = str(name)+"-"+str(frame)+".png"
        img.save(file)
    print("extract img done")