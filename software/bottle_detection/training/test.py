
import cv2
import time

cap=cv2.VideoCapture(1)

time.sleep(2)

print('Frames per seconds: '+str(cap.get(5)))
while True:
            
    ret, img=cap.read()              
    cv2.imshow('test',img)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
                
cap.release()
cv2.destroyAllWindows()
