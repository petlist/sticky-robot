# -*- coding: utf-8 -*-
## Bottle detection with Haar Cascade

import numpy as np
import cv2

def bottle_detection(classifier):
    #classifier is the path to the classifier (.xml) file
    
    bottle_cascade = cv2.CascadeClassifier(str(classifier))
    ## What camera do you use? 0 is std webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #bottles is a vector containing (x,y,w,h) of the detected bottle
        bottles = bottle_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in bottles:
            cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,255),3)
            
            roi_gray = gray[x:x+w,y:y+h]
            roi_color = img[x:x+w,y:y+h]
            #output=[x,y,w,h]
            #return output
                
        
        cv2.imshow('Bottle Detection',img)    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
#bottle_detection('classifiers/training9.xml')


## for commandline use: python3 bottle_detection.py path
if __name__ == "__main__":
    import sys
    bottle_detection(str(sys.argv[1])) 
