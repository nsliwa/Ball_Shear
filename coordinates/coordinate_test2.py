import cv2
import numpy as np
import math

try:
    img = cv2.imread('test_image.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    #minLineLength = 200
    #maxLineGap = 0
    #lines = []

    cv2.imwrite('gray.png',gray)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    # lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    if not lines is None:
        print "found!"
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            
            print x1
            print x2
            print y1
            print y2
            print ""

            d_x = x1 - x2
            d_y = y1 - y2
            d = math.sqrt(d_x * d_x + d_y * d_y)
            print d
            print ""
            print ""
            
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

        #for x1,y1,x2,y2 in lines[0]:
        #    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    else:
        print "none"
    cv2.imwrite('lines.png',img)

    raw_input()

except Exception as ex:
    print ex
    raw_input()
