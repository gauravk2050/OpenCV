'''
adoptive threshold is the method where the threshold is calculated for the smaller region
so the threshold is not global for every pixel so their is different threshold value for different region
we cannot use global threshold value in every case for example
their might be different lighting condition which may varies form point to point thus we there we use
adaptive thresholding technique in that case
'''
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.jpg',0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);

cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()