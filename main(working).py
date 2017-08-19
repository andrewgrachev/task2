import os
import numpy as np
from PIL import Image

# import matplotlib.pyplot as plt
# from skimage import data

def reshape_array(inputArray):
    result = np.zeros((128, 128, 3))

    for i, ar in enumerate(inputArray):
        for j, item in enumerate(inputArray[i]):
            result[i,j,0] = item
            result[i,j,1] = item
            result[i,j,2] = item

    return result

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

    images = []
    print("========================")
    for fname in imlist:
        print(fname)
        image = Image.open(fname)
        print(image)
        resizedImage = image.resize(size)
        print(type(resizedImage))
        imageArrayData = np.array(resizedImage)
        print(type(imageArrayData))
        print(imageArrayData.shape)
        #print(imageArrayData.reshape(128,128,3).shape)

        if imageArrayData.shape == (128, 128):
            imageArrayData = reshape_array(imageArrayData)
            print("EBUSHKI VOROBUSHKI")

        #imageArrayDataReshaped = np.reshape(imageArrayData, (128,128,3))
        #видимо надо тут проверить если это 2д - делать ее в 3д. или
        #момент кое что чекну
        print(imageArrayData.shape)
        if imageArrayData.shape == (128, 128, 3):
            images.append(imageArrayData)
        print("==================")

    arr = np.array(np.mean(images, axis=(0)), dtype=np.uint8)
    out = Image.fromarray(arr)
#    out.save('average.png')
    out.show()

