# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np


def detect(classifier, dtime=10, eps=0.05):
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

            # decide if same or different bottle:
            for i,j in positions:

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


def pixel2angle(pixel, pixel_tot):
    # make numpy arrays
    pixel = np.array(pixel)
    pixel_tot = np.array(pixel_tot)
    # center is angle 0
    pixel_center = pixel_tot / 2
    pixel_new = pixel - pixel_center
    fov_deg = [62.2, 48.8]  # horizontal field of view pi camera in degrees
    fov_rad = np.deg2rad(fov_deg)  # conversion to radians
    angle_rad = (pixel_new / pixel_center) * fov_rad/2
    # angle_deg = (pixel_new / pixel_center) * fov_deg/2
    return angle_rad

indicator, detection_location, pixel_range = detect('classifiers/haarcascade_frontalface_default.xml', 10)

if indicator:
    result = pixel2angle(detection_location, pixel_range)
    print(result)


"""
In the moment the pixels are counted from top left! but should be bottom right! 

Problem solved! Video is flipped.

Wie selemer am schloss dfläsche erkönnne wenns mehreri em beld het? ond wie entscheidemer zo welere zersch go?
idee: alli markiere ond die wo di höchsti ableitig hend, sprech sech am schnellste beweged send am nöchste. Stemmt das??
Ond wie chömemer dethii? idee: alli date sammle för en ziitponkt wo sech de roboter ned bewegt, denn es clustering womer
nor als fläsche alueged wenns mehreri pönkt i nöcher omgäbig het, also ala DBSCAN met outliers. Denn jedes cluster als
ei fläsche beschriibe ond verfolge wie si sech bewegt. Dgrössi chönnt au met canny edge detection gmacht wärde zb. oder 
es gmesch.
"""