import cv2
import numpy as np
import sys

img = cv2.imread('test_image.png',0)

if img==None:
    print "cannot open "

else:
    img = cv2.medianBlur(img,5)
   # cv2.imshow('Blured',img)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
   # cv2.imshow('Blured',cimg)
    
    circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=0,maxRadius=50)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3) # draw the center of the circle
        print(i[0],i[1])


    print(circles.itemsize)    
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.imwrite('output.png',cimg)
    cv2.destroyAllWindows()
