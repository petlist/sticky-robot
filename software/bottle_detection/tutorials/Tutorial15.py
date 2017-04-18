## Background reduction

import numpy as np
import cv2


cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    ## Different Blurs and filters to reduce noise
    kernel = np.ones((15,15),np.float32)/225
    fgmask = cv2.filter2D(fgmask,-1,kernel)
    
    #fgmask = cv2.medianBlur(fgmask,15)
    #fgmask = cv2.GaussianBlur(fgmask,(15,15),0)

    cv2.imshow('true', frame)
    cv2.imshow('mask', fgmask)

     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
