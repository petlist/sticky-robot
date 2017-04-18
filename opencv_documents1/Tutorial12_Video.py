## foreground extraction in videofeed

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    mask = np.zeros(frame.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)

    #foreground needs to be within this rectangle!
    rect = (20, 20, 1000, 700)

    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
    frame = frame*mask2[:,:,np.newaxis]
    cv2.imshow('frame',frame)
##    plt.colorbar()
##    plt.show()

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

