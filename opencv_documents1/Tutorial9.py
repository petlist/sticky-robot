import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #underscore is a dummy variable
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue, saturation, value

    lower_yellow = np.array([20,150,150])
    higher_yellow = np.array([70,255,255])

    mask = cv2.inRange(hsv, lower_yellow, higher_yellow)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # Morphological Transformation

    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(res, kernel, iterations = 1)
    dilation = cv2.dilate(res, kernel, iterations = 1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # other possibilities would be tophat or blackhat

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('Erosion',erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)


    
    # This gives you a video feed until you press q for quitting
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break



cv2.destroyAllWindows()
cap.release()
