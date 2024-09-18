from imagecontroller import ImageController
from imageview import ImageView
from imagemodel import ImageModel

class ImageApp:
    def __init__(self):
        model = ImageModel()
        view = ImageView()
        controller = ImageController(model, view)
        controller.view.root.mainloop()

if __name__ == "__main__":
    ImageApp()