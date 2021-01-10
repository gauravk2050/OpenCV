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

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# Kernal: is the square or some shape which we want to apply on image
kernal = np.ones((5,5), np.uint8)

# Dilation adds pixels to the boundaries of objects in an image
dilation = cv2.dilate(mask, kernal, iterations=2)

#erosion removes pixels on object boundaries
erosion = cv2.erode(mask, kernal, iterations=1)

# opening is the operation in which simply erosion is performed followed by the dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# closing is the operation in which simply dilation is performed followed by the erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# It is the difference between the dilation and erosion of the image
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# It is the difference between image and opening of an image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
