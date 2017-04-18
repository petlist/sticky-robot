## Tutorial 10

import numpy as np
import cv2

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #underscore is a dummy variable
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue, saturation, value
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    lower_yellow = np.array([20,150,150])
    higher_yellow = np.array([70,255,255])

    mask = cv2.inRange(hsv, lower_yellow, higher_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sobelx = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)
    canny = cv2.Canny(gray, 100, 200)
    

    cv2.imshow('frame',gray)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('Canny', canny)

    
    
    # This gives you a video feed until you press q for quitting
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
