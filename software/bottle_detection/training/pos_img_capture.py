# -*- coding: utf-8 -*-
##This file is an automated process of creating positive images once run
##it takes "num" images with a rate of "rate" frames per second. They are
##stored in the folder with the relative path pos_before. For using them
##in a haar training, they need to be treated with the matlabscript main.m
##it is important that each image only contains one bottle.


import numpy as np
import cv2

def pos_grab(num, rate):
    cap=cv2.VideoCapture(0)
    counter=1
    name=0
    
    while True:
        
        ret, img=cap.read()              
        counter=counter+1

        if (counter%rate==0):
            name=name+1
            cv2.imwrite('positives/'+str(name)+'.jpg',img)
            print('positives/'+str(name)+'.jpg saved')
            

        if (name == num):
            print('Process terminated: '+str(name)+' images saved')
            break
            
    cap.release()
    cv2.destroyAllWindows()

#pos_img_capture(15, 5)

## for commandline use: python3 pos_img_capture.py 5 5
if __name__ == "__main__":
    import sys
    pos_img_capture(int(sys.argv[1]), int(sys.argv[2]))

