## Bottle detection with Haar Cascade

import numpy as np
import cv2


gb_cascade = cv2.CascadeClassifier('T5_15.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #gbottles is a vector containing (x,y,w,h) of the face
    gbottles = gb_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in gbottles:
        cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,255),3)
        
        roi_gray = gray[x:x+w,y:y+h]
        roi_color = img[x:x+w,y:y+h]    
            
    
    cv2.imshow('Bottle Detection',img)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
