# -*- coding: utf-8 -*-
import cv2
import time
import numpy as np

import bottle as bt


def detect(classifier, dtime=10, eps=0.05):
    print('quit by hitting "q"!')

    # initialize time
    start_time = time.time()

    # initialize list of bottles
    bottle_list = []

    # initialize bottle counter
    bottle_counter = 0

    # create classifier object
    bottle_cascade = cv2.CascadeClassifier(str(classifier))
    cap = cv2.VideoCapture(0)  # 0 for first camera, 1 for second, etc.
    windowsize = np.array([cap.get(3), cap.get(4)])  # get pixels of frame, e.g. 640x480

    while time.time()-start_time < dtime:
        test_time = time.time()
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # bottles is a vector containing (x,y,w,h) of the detected bottle
        detection_list = bottle_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in detection_list:

            center = np.array([x+w/2, y+h/2])
            if len(bottle_list) == 0:
                print('Bottle list is empty')
                bottle_list.append(bt.Bottle(center, windowsize, '_'.join(['Bottle', str(bottle_counter)])))
                bottle_counter = bottle_counter + 1
                print(bottle_list)
                print('First bottle added\n')
            else:
                distance_list = []

                for b in bottle_list:
                    distance_list.append(b.get_dist(center))
                idx = np.argmin(distance_list)  # find index of smalles distance
                closest_bottle = bottle_list[idx]  # identify closest bottle

                if closest_bottle.part_of_bottle(center):
                    closest_bottle.add_detection_manually(center)
                    bottle_list[idx] = closest_bottle
                    cv2.putText(img, closest_bottle.get_name(), (x, int(y-0.03*windowsize[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255))

                elif not closest_bottle.part_of_bottle(center):
                    bottle_list.append(bt.Bottle(center, windowsize, '_'.join(['Bottle', str(bottle_counter)])))
                    bottle_counter = bottle_counter + 1
                    cv2.putText(img, bottle_list[-1].get_name(), (x, int(y-0.03*windowsize[1])), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 255))
                    print('Bottle added')

            # drawing on image:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)

        # print('time for 1 iteration: ', test_time - time.time())
        cv2.imshow('Bottle Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('quit successfully')
            break

    cap.release()
    cv2.destroyAllWindows()
    return bottle_list


def pixel2angle(pixel, pixel_tot):
    """
    Dont forget to calibrate camera to find exact field of view!
    :param pixel: 
    :param pixel_tot: 
    :return: 
    """
    # make numpy arrays
    pixel = np.array(pixel)
    pixel_tot = np.array(pixel_tot)
    # center is angle 0
    pixel_center = pixel_tot / 2
    pixel_new = pixel - pixel_center
    fov_deg = [62.2, 48.8]  # horizontal field of view pi camera in degrees
    fov_rad = np.deg2rad(fov_deg)  # conversion to radians
    angle_rad = (pixel_new / pixel_center) * fov_rad/2
    angle_deg = (pixel_new / pixel_center) * fov_deg/2
    return angle_deg


def get_list_info(bottle_list, info):
    return_list = []
    for b in bottle_list:
        if info == 'num_det':
            return_list.append(b.get_num_det())
        elif info == 'detections':
            return_list.append(b.get_detections())
        elif info == 'mean':
            return_list.append(b.get_mean())
        elif info == 'windowsize':
            return_list.append(b.get_windowsize())
        elif info == 'status':
            return_list.append(b.get_status())
        elif info == 'name':
            return_list.append(b.get_name())
    return return_list


def validate(bottle_list): # threshold=0.05
    # This function takes a list of bottles and decides which ones are bottles and which ones aren't. It sets the ones
    # that aren't to status "False".
    return_list = []
    list_of_detections = get_list_info(bottle_list, "num_det")
    # print('List of detections: ', list_of_detections)
    number_bottles = len(bottle_list)
    total_detections = sum(list_of_detections)
    # print('total detections: ', total_detections)

    threshold = total_detections/number_bottles

    for idx in range(len(list_of_detections)):
        if list_of_detections[idx] < threshold:
            # print('index ', idx, 'set to False')
            bottle_list[idx].set_status(False)
            # return_list.append(bottle_list[idx])
        elif list_of_detections[idx] >= threshold:
            # print('index ', idx, 'set to True')
            bottle_list[idx].set_status(True)
            return_list.append(bottle_list[idx])
    # print(get_list_info(bottle_list, "status"))

    """
    is it a good idea to modify bottle_list or should I create a new list and copy it? and return this list?
    """
    return return_list

start_time = time.time()

list_of_bottle_detections = detect('classifiers/haarcascade_frontalface_default.xml', 20, 0.01)

print(get_list_info(list_of_bottle_detections, "name"))

list_of_bottles = validate(list_of_bottle_detections)

print(get_list_info(list_of_bottles, "name"))

list_of_means = get_list_info(list_of_bottles, 'mean')

list_of_windowsizes = get_list_info(list_of_bottles, "windowsize")

results = []
for i in range(len(list_of_bottles)):
    results.append(pixel2angle(list_of_means[i], list_of_windowsizes[i]))


print('The final results in degrees are:')

print(results)


"""
In the moment the pixels are counted from top left! but should be bottom right! 

Problem solved! Video is flipped.

Wie selemer am schloss dfläsche erkönnne wenns mehreri em beld het? ond wie entscheidemer zo welere zersch go?
idee: alli markiere ond die wo di höchsti ableitig hend, sprech sech am schnellste beweged send am nöchste. Stemmt das??
Ond wie chömemer dethii? idee: alli date sammle för en ziitponkt wo sech de roboter ned bewegt, denn es clustering womer
nor als fläsche alueged wenns mehreri pönkt i nöcher omgäbig het, also ala DBSCAN met outliers. Denn jedes cluster als
ei fläsche beschriibe ond verfolge wie si sech bewegt. Dgrössi chönnt au met canny edge detection gmacht wärde zb. oder 
es gmesch.


Evtl anstatt zeitfenster, anzahl bilder nehmen! für while loop
"""
