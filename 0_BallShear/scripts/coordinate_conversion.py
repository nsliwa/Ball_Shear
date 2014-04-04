import cv2
import numpy as np
import math
import csv
import sys

try:


    img_package = cv2.imread('../img/package_analyzed.png')
    csv_virtual = open('../data/vcoord.csv', 'r')
    csv_real = open('../data/rcoord.csv', 'w')

    #scaling
    rScale = 7.5            #equal to actual length of scale line
    vScale = 280 #0              #init value
    conversionFactor = 0    #init value

    #origin points
    rOrigin_x = 0   
    rOrigin_y = 0
    vOrigin_x = 75 #0           #init value
    vOrigin_y = 75 #0           #init value

    #coordinates of solder balls
    rCoord_x = 0            #temporary placeholder
    rCoord_y = 0            #temporary placeholder

    #filtering
    h_low = 120
    s_low = 0
    v_low = 0
    h_high = 180
    s_high = 255
    v_high = 255

    hsv_lower = np.array([h_low, s_low, v_low])
    hsv_upper = np.array([h_high, s_high, v_high])


    #################################################
    # identifying scaling line
    #################################################
    # Convert BGR to HSV
    hsv = cv2.cvtColor(img_package, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

    # Bitwise-AND mask and original imagef
    img_filtered = cv2.bitwise_and(img_package,img_package, mask= mask)
    cv2.imwrite('../img/filtered.png',img_filtered)

    # HoughLines Stuff
    gray = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    cv2.imwrite('../img/filtered_gray.png',gray)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    total_l = 0
    num_lines = 0
    
    if not lines is None:
        print "found!"
        for rho,theta in lines[0]:
            a = np.cos(theta)
            print "a:", a
            b = np.sin(theta)
            print "b:", b
            x0 = a*rho
            print "x0:", x0
            y0 = b*rho
            print "y0:", y0
            x1 = int(x0 + 25*(-b))
            y1 = int(y0 + 25*(a))
            x2 = int(x0 - 25*(-b))
            y2 = int(y0 - 25*(a))
            
            print "x1:", x1
            print "x2:", x2
            print "y1:", y1
            print "y2:", y2
            print ""

            cv2.circle(img_package, (x1,y1), 1, (0,0,0), 3)
            cv2.circle(img_package, (x2,y2), 1, (0,0,0), 3)
            cv2.circle(img_package, (75,75), 1, (0,0,0), 3)

            d_x = x1 - x2
            d_y = y1 - y2
            d = math.sqrt(d_x * d_x + d_y * d_y)
            print "length:", d
            print ""
            print ""

            total_l = total_l + d
            num_lines = num_lines + 1
            
            cv2.line(img_package,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.imwrite('../img/filtered_gray_detected.png',img_package)

            if num_lines == 1:
                vOrigin_x = x1
                vOrigin_y = y1
                print "origin: (", vOrigin_x, ",", vOrigin_y, ")"

    # Scaling
        vScale = total_l / num_lines
        print "vScale:", vScale

        print "virtual: (" , vOrigin_x, ",", vOrigin_y, ")"

        print ""
        print ""

        conversionFactor = rScale / vScale

        print "conversionFactor:", conversionFactor
        print ""
        print ""

    #################################################
    # populating virtual coordinates
    #################################################
    # Reading contents of .csv into arrays
        vCoord = np.genfromtxt(csv_virtual, dtype=[('label', 'S5'), ('vCoord_x', 'i8'), ('vCoord_y', 'i8')], delimiter=",")
        for label, vX, vY in vCoord:
            rCoord_x = (vX - vOrigin_x) * conversionFactor
            rCoord_y = (vOrigin_y - vY) * conversionFactor

            csvwriter = csv.writer(csv_real, delimiter=',')
            csvwriter.writerow([label, rCoord_x, rCoord_y])

            print "virtual: (" , vX, ",", vY, ")", "real: (" , rCoord_x, ",", rCoord_y, ")"
        
        csv_real.close()
        csv_virtual.close()

    else:
        print "none found"

    raw_input()

except Exception as ex:
    print ex
    raw_input()
