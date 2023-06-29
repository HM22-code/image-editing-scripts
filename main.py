import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image
import PIL.ImageOps 

class main:

    def __init__(self):
        self.filename = None

        """ Open file dialog and show selected file
        """
    def select_file(self):
        filetypes = (
            ('image files', '.png'),
            ('image files', '.jpg'),
        )

        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=self.filename
        )

        """ Multiplicate an image inside herself
        """
    def multiplicate(self):
        photo=Image.open(self.filename)
        '''On récupere les dimensions de l'image'''
        L,H=photo.size
        iterations=int(input("Entrez le nombre d'itérations"))
        
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

        photo.show()

    def invert(self):
        image=Image.open(self.filename)
        image2 = PIL.ImageOps.invert(image)
        image2.show()

        """ Remove white pixel and replace it with transparent pixel
        """
    def transparancy(self):
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

    def run(self):
        # create the root window
        root = tk.Tk()
        root.title('Tkinter Open File Dialog')
        root.resizable(False, False)
        root.geometry('300x150')
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

        # pack widgets
        open_button.pack(expand=True)
        multiplicate_button.pack(expand=True)
        invert_button.pack(expand=True)
        transparency_button.pack(expand=True)


        # run the application
        root.mainloop()

if __name__ == '__main__':
    main().run()



