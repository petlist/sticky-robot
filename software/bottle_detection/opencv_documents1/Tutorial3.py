import numpy as np
import cv2
#from matplotlib import pyplot as plt

# Read image
img = cv2.imread('singapore2.jpeg',cv2.IMREAD_COLOR)

cv2.line(img,(10,10),(150,150),(255,0,255),20)
cv2.rectangle(img,(10,10),(200,100),(255,0,0),10)
cv2.circle(img, (50,50), 30, (255,255,255),5)

# Draw a Polygon

pts = np.array([[1,1],[100,100],[100,50],[50,50],[50,100]],np.int32)
cv2.polylines(img,[pts], True, (0,0,255),2 )

# How to write

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'hello', (100,100) ,font ,1 ,(0,0,0) ,2 ,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
