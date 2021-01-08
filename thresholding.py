'''
Thresholding is the segmentation technique used for separating  the object from its background
The process of thresholding involves comparing each pixel of an image with a predifined threshold values.

The method returns two outputs. The first is the threshold that was used and the second output is the thresholded image
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('images.jpg', 0)
# threshod gives result in two values ret value and another one is threshold value
#threshold(source,minimum threshold pixel,maximum threshold pixel,type of threshold)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
'''
Binary threshold comparies this original image to 127 and is the value of the pixel
is less then 127 the value is assigned to 0 and if the value of the pixel is more then 
 127 the value is assigned to 1
 0=black
 1=white
 '''
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
#the give the inverse result what you get from therss binary

_, th3 = cv.threshold(img, 200, 255, cv.THRESH_TRUNC)
# In this upto the threshold value the pixel value will not be change but after the threshold value the pixel will remain the threshold value i.e here 200

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# cv.imshow("Image", img)
# cv.imshow("th1",th1)
# cv.imshow("th2",th2)
# cv.imshow('th3',th3)
# cv.imshow("th4", th4)
# cv.imshow("th5", th5)

# cv.waitKey(0)
# cv.destroyAllWindows()

plt.show()
