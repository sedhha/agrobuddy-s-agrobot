#Fading
#Zooming
#Rotating
import numpy as np
import cv2
cam=cv2.VideoCapture(0)
while True:
    cret,frame=cam.read()
    b,g,r=cv2.split(frame)
    b=b*0.9
    g=g*0.9
    r=r*0.9
    cv2.imshow('cam',b+g+r)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
