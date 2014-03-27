import cv2
import numpy as np



def nothing(x):
    pass

cap = cv2.VideoCapture(2)



# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H','image',0,180,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)

cv2.createTrackbar('H_low','image',0,180,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)

while(1):

    # Take each frame
    _, frame = cap.read()
   
    # get current positions of four trackbars
    h = cv2.getTrackbarPos('H','image')
    s = cv2.getTrackbarPos('S','image')
    v = cv2.getTrackbarPos('V','image')
   
    h_low = cv2.getTrackbarPos('H_low','image')
    s_low = cv2.getTrackbarPos('S_low','image')
    v_low = cv2.getTrackbarPos('V_low','image')
    

  

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower = np.array([h_low,s_low,v_low])
    upper = np.array([h,s,v])
    #lower = np.array([110,50,50])
    #upper = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
