import os, math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

Dir = input("Dir: ")

try:
    K = int(input('inpit K:'))
except (SyntaxError, ValueError):
    K = 16

try:
    S = tuple(int(x.strip()) for x in input('Input S:').split(','))
except (SyntaxError, ValueError):
    S = 128, 128


def reshape_array(inputArray):
    result = np.zeros((size[1], size[0], 3))

    for i, ar in enumerate(inputArray):
        for j, item in enumerate(inputArray[i]):
            result[i, j, 0] = item
            result[i, j, 1] = item
            result[i, j, 2] = item

    return result


allimages = []
os.chdir(Dir)
choices = []
directory = os.listdir(Dir)
choices = np.random.choice(directory, K, replace=False)
dIrects = []
figures = {}

for dIrect in choices:
    os.chdir(Dir + "/" + dIrect)
    # dIrect = title for subplot
    dIrects.append(dIrect)
    allfiles = os.listdir(os.getcwd())
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg", ".JPG"]]
    size = S
    arr = np.zeros((size[1], size[0], 3), np.float)
    images = []

    for fname in imlist:
        image = Image.open(fname)
        resizedImage = image.resize(size)
        imageArrayData = np.array(resizedImage)

        if imageArrayData.shape == (size[1], size[0]):
            imageArrayData = reshape_array(imageArrayData)

        if imageArrayData.shape == (size[1], size[0], 3):
            images.append(imageArrayData)

    arr = np.array(np.mean(images, axis=(0)), dtype=np.uint8)
    out = Image.fromarray(arr)
    allimages.append(arr)
    figures[dIrect] = out
    # out.show()

Nr = round(math.sqrt(K))
Nc = round(math.sqrt(K))
if Nr + Nc > K:
    Nr = Nr + 1


def plot_figures(figures, nrows=Nr, ncols=Nc):
    fig, axeslist = plt.subplots(ncols=ncols, nrows=nrows)
    for ind, title in zip(range(len(figures)), figures):
        axeslist.ravel()[ind].imshow(figures[title])
        axeslist.ravel()[ind].set_title(title)
        axeslist.ravel()[ind].set_axis_off()
    # plt.tight_layout() # optional
    plt.show()


plot_figures(figures, Nr, Nc)
