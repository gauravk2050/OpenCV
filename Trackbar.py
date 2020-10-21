'''
Trackbar are useful in openCV whenever you want to change any value in your image dynamically at one time
'''

import cv2 as cv
import numpy as np

# function to print the changed value of BGR
def nothing(x):
    print(x)

# create a black image window
img = np.zeros((300,512,3),np.uint8)
cv.namedWindow('image') # create a window with a name

# Creating treckbar
cv.createTrackbar('B','image',0,255, nothing)
'''
B : Blue color
image : name of the window in which we need to create trackbar
0 : stating value 
255: ending value
nothing : what function is to be performe

similarly creating tracker for green and red
'''
cv.createTrackbar('G','image',0,255, nothing)
cv.createTrackbar('R','image',0,255, nothing)

'''
Creating Switch button 
it switch button will be 1 then you can change the color using tracker 
if switch will be 0 then you cant do
'''
switch='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'image',0,1, nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()