# -*- coding: utf-8 -*-
##This file is an automated process of creating positive images once run
##it takes "num" images with a rate of "rate" frames per second. They are
##stored in the folder with the relative path pos_before. For using them
##in a haar training, they need to be treated with the matlabscript main.m
##it is important that each image only contains one bottle.

import cv2
import os

def foldercheck(mode):
    if mode=='neg':
        if not os.path.exists('negatives'):
            os.makedirs('negatives')
            print('directory \'negatives\' made')
    if mode=='pos':
        if not os.path.exists('positives_to_process'):
            os.makedirs('positives_to_process')
            print('directory \'positives_to_process\' made')

def create_neg():
    for img in os.listdir('negatives/'):
        try:
            line = 'negatives/'+str(img)+'\n'
            with open('neg.txt','a') as f:
                f.write(line)
        except Exception as e:
            print(str(e))    

def grab(mode, num, rate):
    ## mode: pos neg
    ## num: number of images wanted
    ## rate: every 'rate' seconds a image is saved
    cap=cv2.VideoCapture(0)
    fps=cap.get(5) #5th option is frames per seconds
    counter=1
    name=0
    
    while True:
        
        ret, img=cap.read()              
        counter=counter+1
        if mode == 'pos':
            if (counter%(fps*rate)==0):
                name=name+1
                cv2.imwrite('positives_to_process/'+str(name)+'.jpg',img)
                print('positives_to_process/'+str(name)+'.jpg saved')
        if mode == 'neg':
            if (counter%(fps*rate)==0): 
                name=name+1
                cv2.imwrite('negatives/'+str(name)+'.jpg',img)
                print('negatives/'+str(name)+'.jpg saved')
                        
        if (name == num):
            print('Process terminated: '+str(name)+' images saved')
            break
            
    cap.release()
    cv2.destroyAllWindows()

## for commandline use: python3 pos_img_capture.py pos 5 5
if __name__ == "__main__":
    import sys
    foldercheck(str(sys.argv[1]))
    grab(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    if str(sys.argv[1])=='neg':
        create_neg()   

