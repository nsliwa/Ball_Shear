import cv2
import numpy as np
import math

try:
    img = cv2.imread('test_image.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    cv2.imwrite('gray.png',gray)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    total_l = 0
    num_lines = 0

    vlength = 0
    rlength = 11

    origin_vx = 0
    origin_vy = 0
    origin_rx = 0
    origin_ry = 0

    coord_vx = []
    coord_vy = []
    coord_rx = []
    coord_ry = []
    
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

            total_l = total_l + d
            num_lines = num_lines + 1
            
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

            if num_lines == 1:
                origin_vx = x1
                origin_vy = y1

            else:
                coord_vx.append(x1)
                coord_vx.append(x2)
                coord_vy.append(y1)
                coord_vy.append(y2)

        vlength = total_l / num_lines
        print vlength

        print "(" , origin_vx, ",", origin_vy, ")"

        print ""
        print ""

        distance = rlength / vlength

        for index in range(len(coord_vx)):
            coord_rx.append((origin_vx - coord_vx[index]) * distance)
            coord_ry.append((origin_vy - coord_vy[index]) * distance)

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,"index",(coord_vx[index],coord_vy[index]), font, 4,(255,255,255),2)
            #cv2.putText(img,"1",(100,50), font, 4,(20,25,55),2)
            
            print "(" , coord_vx[index], ",", coord_vy[index], ")", "(" , coord_rx[index], ",", coord_ry[index], ")"
        
    else:
        print "none"
    cv2.imwrite('lines.png',img)

    raw_input()

except Exception as ex:
    print ex
    raw_input()
