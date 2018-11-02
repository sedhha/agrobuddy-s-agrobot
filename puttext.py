import cv2
import numpy as np

img=cv2.imread(r'E:\SAHIL\RW\SpiderBot\images\5.JPG')
text="Success"
cv2.putText(img, text, (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), lineType=cv2.LINE_AA)
cv2.imshow('I',img)
