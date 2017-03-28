import numpy as np
import cv2

img = cv2.imread('bookpage.jpg',cv2.IMREAD_COLOR) #read image

img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to grayscale

retval, threshold = cv2.threshold(img2gray,14,255,cv2.THRESH_BINARY) #apply threshold

# Gaussian adaptive threshold
gaussian = cv2.adaptiveThreshold(img2gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('gaussian',gaussian)
cv2.imshow('Bookpage',img)
cv2.imshow('Bookpage_Threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

