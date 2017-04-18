import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #underscore is a dummy variable
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue, saturation, value

    lower_yellow = np.array([60,100,100])
    higher_yellow = np.array([80,255,255])

    mask = cv2.inRange(frame, lower_yellow, higher_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # blurring and smoothing
    avgnumb = 15
    kernel = np.ones((avgnumb,avgnumb), np.float32)/(avgnumb*avgnumb)
    smoothed = cv2.filter2D(res, -1, kernel)

    blurgaus = cv2.GaussianBlur(res, (avgnumb,avgnumb), 0)

    median = cv2.medianBlur(res,avgnumb)

    #bilateral = cv2.bilateralFilter(res,avgnumb,75,75)


    # Morphological Transformation
    

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('smoothed',smoothed)
    cv2.imshow('Gaussian Blur', blurgaus)
    cv2.imshow('Median Blur', median)

    # This gives you a video feed until you press q for quitting
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

##    # This gives you a new frame whenever you press a key
##    k = cv2.waitKey(0) & 0xFF
##    if k == 27:
##        break

cv2.destroyAllWindows()
cap.release()
