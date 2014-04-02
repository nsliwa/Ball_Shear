#import cv2
import numpy as np
import math
import csv

try:
#    img_package = cv2.imgread('package_analyzed.png')
    csv_virtual = open('vcoord.csv', 'r')
    csv_real = open('rcoord.csv', 'w')

    #scaling
    rScale = 7.5            #equal to actual length of scale line
    vScale = 280 #0              #will be reset to correct val
    conversionFactor = 0    #will be reset to correct val

    #origin points
    rOrigin_x = 0   
    rOrigin_y = 0
    vOrigin_x = 75 #0           #will be reset to correct val
    vOrigin_y = 75 #0           #will be reset to correct val

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

    # Scaling
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
        csvwriter.writerow([label, rCoord_x, rCoord_y])

        print "(" , vX, ",", vY, ")", "(" , rCoord_x, ",", rCoord_y, ")"
        
    csv_real.close()
    csv_virtual.close()

    raw_input()

except Exception as ex:
    print ex
    raw_input()
