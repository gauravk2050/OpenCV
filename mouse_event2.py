# Dont know waht is the error program is corrrect accorsing to me bt it is not giving proper result
# Video also not having code.
# This Program is to open the new window of the color which you have clicked on a image 
import numpy as np
import cv2

'''
# itterating all events availabele in cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
'''


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue=img[x, y, 0]
        green =img[x, y, 1]
        red = img[x, y, 2]
        cv2.circle(img,(x, y),3,(0,0,255),-1)# here -1 will fill the image with the given color
        mycolorImage = np.zeros((512,512,3), np.unit8)
         
        # points.append((x,y))
        mycolorImage[:] = [blue,green, red]

        # if len(ponints) >=2:
        #     cv2.line(img,points[-1], points[-2], (255, 0 , 0), 5)

        # cv2.imshow('image',img)
        cv2.imsgow('color',mycolorImage)
        

    
  
img = np.zeros((512, 512, 3), np.uint8)
# img = cv2.imread('lena.jpg')
cv2.imshow('image', img)

points=[]

#this method is used to call the function for a mouse event
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
