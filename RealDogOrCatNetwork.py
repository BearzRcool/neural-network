import numpy as np
import PIL

cat = "PetImages\cat.png"
dog = "PetImages\dog.png"

from PIL import Image

with Image.open(cat) as im:
    px = im.load()
    width, height = im.size
    get_image = im.getdata()


    array = np.array(get_image)
    print(array)
    

    