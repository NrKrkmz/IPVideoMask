import numpy as np
import cv2
cap = cv2.VideoCapture(0)

param1 = [100,100,100] 
param2 = [150,150,255]

while(1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower = np.array(param1)    
    upper = np.array(param2)
    mask  = cv2.inRange(hsv, lower, upper) 
    res   = cv2.bitwise_and(frame, frame, mask= mask)
    
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    

    if cv2.waitKey(1) == 27:  
        break

cap.release()
cv2.destroyAllWindows()