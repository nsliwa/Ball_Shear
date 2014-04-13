import cv2,sys

vc = cv2.VideoCapture(2)

if not(vc.isOpened()): # try to get the first frame
    print >> sys.stderr, 'Camera is not detected . Please plug in camera'
