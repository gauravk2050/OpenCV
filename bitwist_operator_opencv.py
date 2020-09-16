'''
Mask are the bimary images in which indicates the pixcels on which operation is to be performed
'''
import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1=cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2=cv2.imread("download.png")

# resizing both images so that operatin can perform as operation can only perform between the images of equal sizes
img1=cv2.resize(img1,(512,512))
img2=cv2.resize(img2,(512,512))

bitAnd = cv2.bitwise_and(img2, img1)
'''
it perform the AND operation
black = 0
white = 1 
black and black = black(0)
white and white = white(1)
black and white = black(0)
white and black = black(0)
'''

bitOr = cv2.bitwise_or(img2, img1)
'''
it perform the Logical OR operation
black = 0
white = 1 
black and black = black(0)
white and white = white(1)
black and white = white(1)
white and black = white(1)
'''

#similarly
bitXor=cv2.bitwise_xor(img1,img2)
bitNot1=cv2.bitwise_not(img1)
bitNot2=cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOr',bitOr)
cv2.imshow('bitXor',bitXor)
cv2.imshow('bitNot1',bitNot1)
cv2.imshow('bitNot2',bitNot2)



cv2.waitKey(0)
cv2.destroyAllWindows()



