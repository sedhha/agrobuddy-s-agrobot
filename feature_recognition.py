import numpy as np
import cv2
from matplotlib.pyplot import subplot,imshow,show,figure,pause
cap=cv2.VideoCapture(0)
img1=cv2.imread('about-us.jpg')
sift=cv2.xfeatures2d.SIFT_create()
surf=cv2.xfeatures2d.SURF_create()
kp1,desc1=sift.detectAndCompute(img1,None)
img=cv2.drawKeypoints(img1,kp1,img1)
index_params = dict(algorithm = 0, trees = 5)
search_params = dict(checks = 50)
flann=cv2.FlannBasedMatcher(index_params,search_params)
while True:
    ret,frame=cap.read()
    #imshow(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kp2,desc2=sift.detectAndCompute(gray,None)
    matches=flann.knnMatch(desc1,desc2,k=2)
    good=[]
    for m,n in matches:
        if m.distance<0.6*n.distance:
            good.append(m)
    img3=cv2.drawMatches(img,kp1,gray,kp2,good,None)
    if (len(good))>10:
        try:
            query_pts=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
            train_pts=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
            matrix,mask=cv2.findHomography(query_pts,train_pts,cv2.RANSAC,5.0)
            match_mask=mask.ravel().tolist()
            h,w=np.shape(cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY))
            pts=np.float32([[0,0],[0,h],[w,h],[w,0]]).reshape(-1,1,2)
            dst=cv2.perspectiveTransform(pts,matrix)
            #print(dst)
            homography=cv2.polylines(frame,[np.int32(dst)],True,(255,0,0))
            cv2.imshow('homography',homography)
            
        except:
            pass
    else:
        cv2.imshow('homography',gray)
    cv2.imshow('img3',img3)
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
