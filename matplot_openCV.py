# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('lena.jgp', -1)
# cv2.imshow('image',img)
# img= cv2.cvtcolor(img,cv2.COLOR_BGR2RBG)
#
# plt.imshow(img)
# plt.xticks([]), plt.yticks([]) # this will hide the x and y axis coordinates form the image
# plt.show()
#
# cv2.WaitKey(0)
# cv2.destroyAllWindows()

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()