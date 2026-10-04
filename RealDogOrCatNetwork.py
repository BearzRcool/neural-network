import numpy as np
import PIL

cat = "PetImages\cat.png"
dog = "PetImages\dog.png"

from PIL import Image
def ProcessImage(image):
    with Image.open(image) as im:
        px = im.load()
        width, height = im.size
        get_image = im.getdata()


        return np.array(get_image), width, height






    