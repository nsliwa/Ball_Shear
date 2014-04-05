import cv2
import numpy as np
import math
import csv
import sys
import Image

try:


    img_package = cv2.imread('../img/package_analyzed.png')
    csv_virtual = open('../data/vcoord.csv', 'r')
    csv_real = open('../data/rcoord.csv', 'w')

    #dimensions
    height, width, depth = img_package.shape

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

    pic = Image.open('../img/filtered_gray.png')
    width, height, = pic.size

    for y in range(70, 80):
        for x in range(70, 375):
            print "(", x, ",", y, "):", pic.getpixel( (x,y) ) #print "(", x, ",", y, "):", img_package[x,y], ",", gray[x,y]
        print ""

    cv2.imwrite('../img/filtered_gray.png',gray)

    raw_input()

except Exception as ex:
    print ex
    raw_input()