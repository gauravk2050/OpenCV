'''
MORPHOLOGICAL TRANSFORMATIONS: These are some simple operation based on image shape.
these are normaly performed on a binary image 
Things required for transformation are
1.original image 
2.structuring element(kernal) - It tells you how to change the values of any pixel by combining it with different amount of ht eneighbour pixel.
'''

import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)

title = ['image']
image = [img]

for i in range(1):
    plt.subplot(1, 1, i+1)
    plt.show(image[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()