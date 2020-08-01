import cv2
'''
sc2.imread() Second argument flag is for
1 - Loads colour image
0 - Loads image in grayscale mode
-1 - Loads image as such includeing alpha channel
'''
img = cv2.imread('lena.jpg', 1)

cv2.imshow('image', img)               # showing image
k = cv2.waitKey(5000)                  # image will be there for 5 sec

if k == 27:                            # windows will be destroyed if we press Esc (27 is the value of Esc)
    cv2.destroyAllWindows()            # window will be destroyed after 5 sec

elif k == ord('s'):                    # Press s to save the image
    cv2.imwrite('lena_copy.png', img)  # Write the copy of image
    cv2.destroyAllWindows()