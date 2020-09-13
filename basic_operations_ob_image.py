import numpy as np
import cv2

img=cv2.imread('image.jpg')
img2=cv2.imread('opencv-logo.png')

print(img.shape) # return the tuple of number of rows ,columns, and channels
print(img.size)    # return total number of pixels in accessed
print(img.dtype) # return In=mage datatype is obtained

b,g,r = cv2.split(img) # spliting your image into 3 channels
img = cv2.merge((b,g,r)) # if you are having b,g,r channel and you want to merge then you can use merge() method

# Copying the football to another place
'''
1st know the cordinates of the object
2nd know the cordinates where the object have to be coppied
knowing the cordinates of the object can be done using privious program mouse_events_opencv.py
'''

# ball = img[641:622, 658:619]
# img[195:943, 234:489] = ball

'''
Adding two images by using add method
For adding two images the size or the image or array should be same
so firstly resizeing the image for adding two image using cv2.resize()'''

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

# dst=cv2.add(img2,img)

'''
Another method for adding the two image 
with this method you can decide the waitage of image 
dst(I)=saturate(source(I)*alpha+sourc2(I)*beta+gamma)
the method is addWeighted(source1,weight1,source2,weight2,gamma)...gamma is th e scale value
'''

dst=cv2.addWeighted(img, .9, img2, .1, 0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()