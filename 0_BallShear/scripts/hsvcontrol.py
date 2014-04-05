# -*- coding: cp1252 -*-
import cv2
import numpy as np
import time 


def nothing(x):
    pass

# Create a black image, a window
img = cv2.imread('../img/package6.png')
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H_low','image',0,180,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)

cv2.createTrackbar('H_high','image',0,180,nothing)
cv2.createTrackbar('S_high','image',0,255,nothing)
cv2.createTrackbar('V_high','image',0,255,nothing)

date_string=time.strftime("%Y%m%d_%H%M.png")
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF


    # get current positions of four trackbars
    h_low = cv2.getTrackbarPos('H_low','image')
    s_low = cv2.getTrackbarPos('S_low','image')
    v_low = cv2.getTrackbarPos('V_low','image')
    
    h_high = cv2.getTrackbarPos('H_high','image')
    s_high = cv2.getTrackbarPos('S_high','image')
    v_high = cv2.getTrackbarPos('V_high','image')
    
    

    lower = np.array([h_low,s_low,v_low])
    upper = np.array([h_high,s_high,v_high])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if k == 27:
        file = date_string
        cv2.imwrite(file,res)
        break
    
cv2.destroyAllWindows()
