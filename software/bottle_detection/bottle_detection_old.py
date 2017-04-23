# -*- coding: utf-8 -*-
## Bottle detection with Haar Cascade

import cv2

class BottleDetection:
    """This class is responsible for the bottle detection!"""
    def __init__(self, classifier, cam = 0):
        # classifier is the path to the xml file of the classifier
        # cam is an integer to choose the camera input
        self.classifier = classifier
        self.cam = cam

    def testing(self):
        """testing function to see if class works"""
        print('test successful')


    def detect(self):
        # Information about quitting
        print("Press 'q'-key to exit")
        #classifier is the path to the classifier (.xml) file

        bottle_cascade = cv2.CascadeClassifier(str(self.classifier))
        ## What camera do you use? 0 is std webcam
        cap = cv2.VideoCapture(self.cam)

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
## for commandline use: pythons3 bottle_detection_old.py path

test = BottleDetection('classifiers/training9.xml',1)
test.detect()
if __name__ == "__main__":
    import sys
    print('Access via command line')
    BottleDetection.detect(str(sys.argv[1]))
