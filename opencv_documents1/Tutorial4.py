import cv2
import numpy as np

img_0 = cv2.imread('singapore2.jpeg',cv2.IMREAD_COLOR)
#img = cv2.cvtColor(img_0, cv2.


# Pixel
img_0[55,55]=[255,255,255]
px = img_0[55,55]
px = [255,255,255]


# Region of Image
img_0[100:150,100:150] =[255,255,255]
roi = img_0[37:111,107:194]
img_0[0:74,0:87]=roi

cv2.imshow('image',img_0)
cv2.waitKey(0)
cv2.destroyAllWindows()

 
