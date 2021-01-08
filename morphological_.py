'''
Morphological transformation are some simple operation based on the image shape.
it is normally perform on binary image
To perform this image we need two things 1st an original image , 2nd structuring welement or kernal
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)

title = ['image']
image = [img]

for i in range(1):
    plt.subplot(1,1,i+1),plt.imshow(image[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()