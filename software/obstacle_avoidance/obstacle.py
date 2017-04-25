import numpy as np


class Obstacle:
    def __init__(self, initial, imagesize, name='bottle'):
        self.obstacle = np.array([initial])  # numpy array with detections of the bottle, initial is the first detection
        self.status = True  # can the instance be considered as a bottle or is it an outlier?
        self.mean = np.rint(np.mean(self.obstacle, axis=0))  # mean of bottle detection
        self.eps = 0.05  # epsilon such that detection is counted as the same bottle
        self.imagesize = np.rint(imagesize)  # image dimensions that are being analyzed: [width, height] or np.array
        self.name = name
        print('Name of new bottle is: ', self.name)

    def get_status(self):
        return self.status

    def get_detections(self):
        return self.obstacle

    def get_mean(self):
        self.mean = np.rint(np.mean(self.obstacle, axis=0))  # update mean
        return self.mean

    def get_num_det(self):
        return np.size(self.obstacle, axis=0)

    def get_windowsize(self):
        return self.imagesize

    def get_dist(self, detection):
        dist = np.sqrt(np.sum((self.obstacle - detection) ** 2, axis=1))
        idx_min = np.argmin(dist)
        min_dist = dist[idx_min]
        return min_dist

    def get_name(self):
        return self.name

    def set_eps(self, eps):
        self.eps = eps
        print(' '.join(['Epsilon set to', str(eps)]))

    def set_status(self, status):
        if status == 'on' or status == True:
            print('Status of ', self.name, 'set to True')
            self.status = True
        elif status == 'off' or status == False:
            print('Status of ', self.name, 'set to False')
            self.status = False

    def part_of_bottle(self, detection):
        if self.get_dist(detection) <= self.eps * self.imagesize[0]:
            print(' '.join(['This detection is part of', self.name]))
            return True
        else:
            print(' '.join(['This detection is not part of', self.name]))
            return False

    def add_detection_manually(self, detection):
        print(detection)
        detection_2d = np.array([detection])  # bring detection into right dimensions
        self.obstacle = np.concatenate((self.obstacle, detection_2d), axis=0)
        #print(' '.join(['Detection', detection, 'added to', self.name])) doesnt work! because of detection

    def add_detection(self, detection):  # actually not needed! check if part of bottle outside class
        if self.part_of_bottle(detection):
            self.add_detection_manually(detection)
            return True
        else:
            print('The detection is not part of the bottle')
            return False

