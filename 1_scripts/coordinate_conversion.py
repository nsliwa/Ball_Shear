import cv2
import numpy as np
import math
import csv

try:
    img_package = cv2.imgread('package_analyzed.png')
    csv_virtual = open('vcoord.csv', 'r')
    csv_real = open('rcoord.csv', 'w')

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
    S_low = 0
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
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    img_filtered = cv2.bitwise_and(img,img, mask= mask)
    cv2.imwrite('filtered.png',img_filtered)

    # HoughLines Stuff
    gray = cv2.cvtColor(img_filtered, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    cv2.imwrite('filtered_gray.png',gray)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    total_l = 0
    num_lines = 0
    
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
                vOrigin_x = x1
                vOrigin_y = y1

    # Scaling
        vScale = total_l / num_lines
        print vScale

        print "(" , vOrigin_x, ",", vOrigin_x, ")"

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
            csvwriter.writerow([label, rCoord_x, rCoord_y)

            print "(" , vX, ",", vY, ")", "(" , rCoord_x, ",", rCoord_y, ")"
        
        csv_real.close()
        csv_virtual.close()

    else:
        print "none found"

    raw_input()

except Exception as ex:
    print ex
    raw_input()
