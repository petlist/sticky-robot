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




def detect_old(classifier, dtime=10, eps=0.05):
    print('quit by hitting "q"!')
    # initialize counters and positions vector
    detection_counter = 0
    bottles_counter = 0
    positions = np.array([[0, 0]])
    success = False

    # initialize time
    start_time = time.time()

    # create classifier object
    bottle_cascade = cv2.CascadeClassifier(str(classifier))
    cap = cv2.VideoCapture(0)  # 0 for first camera, 1 for second, etc.
    pixel_tot = np.array([cap.get(3), cap.get(4)])  # get pixels of frame, e.g. 640x480

    while time.time()-start_time < dtime:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # bottles is a vector containing (x,y,w,h) of the detected bottle
        bottles = bottle_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in bottles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)
            center = np.array([[x+w/2, y+h/2]])

            """
            # decide if same or different bottle:
            for bot in positions:  # bot are the different bottles, j the detections per bottle, k detections pixels
                #for det in bot:

                dist = (bot - center) ** 2
                dist = np.sum(dist, axis=1)
                dist = np.sqrt(dist)
                idx_min = np.argmin(dist)
                # detection belongs to the bottle
                if dist[idx_min] <= eps:
                    positions = np.concatenate((positions, center), axis=1)
                    detection_counter
            """
            """
            Problem: like this the number of detections for every bottle need to be the same since the array must be 
            rectangular!
            Solution: make class bottle and everytime a new detection is made create a new instance of bottle!
            """

            positions = np.concatenate((positions, center), axis=0)
            detection_counter = detection_counter + 1

        cv2.imshow('Bottle Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('quit successfully')
            break
    cap.release()
    cv2.destroyAllWindows()

    positions = np.delete(positions, 0, axis=0)  # to delete 0 row of initialization. Had problems with concatenate!

    # make return
    if detection_counter == 0:
        print('No bottles have been detected')
        return success, np.array([[-1,-1]]), np.array([-1,-1])
    else:
        success = True
        mean = np.rint(np.mean(positions, axis=0))
        return success, mean, pixel_tot
