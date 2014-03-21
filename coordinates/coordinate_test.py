import cv2
import numpy as np

try:
    img = cv2.imread('test_image.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 200
    maxLineGap = 5
    lines = []
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    if not lines is None:
        print "found!"
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    else:
        print "none"
    cv2.imwrite('houghlines5.png',img)

except Exception as ex:
    print ex
    raw_input()
