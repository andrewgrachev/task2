import os
import numpy as np
from PIL import Image

# import matplotlib.pyplot as plt
# from skimage import data

S = 128, 128
K = 16

Dir = input("Dir: ")
#K = int(input('inpit K:'))
#S = tuple(int(x.strip()) for x in input('Input S:').split(','))

# /home/andrew/okas/task2/101_ObjectCategories
os.chdir(Dir)
choices = []

directory = os.listdir(Dir)
choices = np.random.choice(directory, K)

for dIrect in choices:
    os.chdir(Dir + "/" + dIrect)
    allfiles = os.listdir(os.getcwd())
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg", ".JPG"]]
    size = S

    arr = np.zeros((size[1], size[0], 3), np.float)

    images = np.array([np.array(Image.open(fname).resize(size)) for fname in imlist])
    arr = np.array(np.mean(images, axis=(0)), dtype=np.uint8)
    out = Image.fromarray(arr)
#    out.save('average.png')
    out.show()
