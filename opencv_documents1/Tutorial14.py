import numpy as np
import cv2
import matplotlib.pyplot as plt

img2 = cv2.imread('scene2.jpg',0)
img1 = cv2.imread('greenbottle2.jpg',0)
##img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
##img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

orb = cv2.ORB_create() #create detector
kp1, des1 = orb.detectAndCompute(img1,None) #keypoints and descriptors
kp2, des2 = orb.detectAndCompute(img2,None)

#find keypoints
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
#find matches and sort them based on confidence
matches = bf.match(des1,des2) 
matches = sorted(matches, key=lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:300], None, flags=2)

plt.imshow(img3)
plt.show()

##cv2.imshow('scene',img1)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
