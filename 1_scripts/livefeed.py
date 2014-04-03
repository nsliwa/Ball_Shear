import cv2
import sys

cv2.namedWindow("Live Feed")
vc = cv2.VideoCapture(2)

img_package = str(sys.argv[1])

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = vc.read()
 return im

def capture():
	camera_capture = get_image()
	file = img_package #"test_image.png"
	cv2.imwrite(file, camera_capture)
	display()

def display():
	print("Press ESC to Delete")
	print("Press S to Save")
	imgFile = cv2.imread(file) #'test_image.png')
	cv2.imshow('image', imgFile)
	key = cv2.waitKey(0)
	if key == 27: cv2.destroyWindow('image')	
	if key == 115:cv2.destroyAllWindow()

print("Press c to capture a Image")
while rval:
    cv2.imshow("Live Feed", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)

    #key2 = cv2.waitKey(0);
    if key == 27: # exit on ESC
        break
    if key == 99:
    	capture()
		
cv2.destroyWindow("preview")
