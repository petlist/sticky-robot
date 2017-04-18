import numpy as np
import cv2

img1 = cv2.imread('sg_gbb.jpg')
img2 = cv2.imread('sg_city.jpg')
img3 = cv2.imread('bottles.jpeg')


# Adding images together
#add = img1 + img2
#add=cv2.add(img1,img2)
add = cv2.addWeighted(img1,0.1,img2,0.9,0)

## Mask and add image

# Create ROI
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

# Create Mask
img2gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3,img3,mask=mask)
dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols]=dst

##cv2.imshow('test',img1_bg)
##cv2.imshow('test2',img3_fg)
##cv2.imshow('img',img1)
cv2.imshow('mask',mask_inv)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()


