import cv2,sys
import numpy as np
cv2.namedWindow("Live Feed")
vc = cv2.VideoCapture(2)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False
    print >> sys.stderr, 'Camera is not detected . Please plug in camera'


# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = vc.read()
    return im

def capture():
    camera_capture = get_image()
    print(len(sys.argv))
    if(len(sys.argv)==1):
        file="package.png"
    else:
        file = sys.argv[1]
    (h, w) = camera_capture.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    rotated = cv2.warpAffine(camera_capture, M, (w, h))    
    camera_capture= rotated
    cv2.imwrite(file, camera_capture)
    a =display()
    if(a == 2):return 2

def display():
    print("Press ESC to Delete")
    print("Press S to Save")
    if(len(sys.argv)==1):
        imgFile=cv2.imread('package.png')
        cv2.imshow('image', imgFile)
    else:
        imgFile = cv2.imread(sys.argv[1])
        cv2.imshow('image', imgFile)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyWindow('image')
        return 1
    if key == 115:
        cv2.destroyWindow('image')
        cv2.destroyWindow("Live Feed")
        return 2
        
	


if(len(sys.argv)!=2):
        print >> sys.stderr, 'Input argument is not found'
        rval=0
else:
    print("Press c to capture a Image")
#print(sys.argv[1])
while rval:
        cv2.imshow("Live Feed", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        b=0
    #key2 = cv2.waitKey(0);
    
        if key == 27: # exit on ESC
            print >> sys.stderr, 'Picture has not been saved. Please take image again'
            break
        if key == 99:
            b =capture()
        if (b==2):
            break
    	
    	
    
		
cv2.destroyWindow("Live Feed")

