import cv2,sys
cv2.namedWindow("Live Feed")
vc = cv2.VideoCapture(2)

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
    print(len(sys.argv))
    if(len(sys.argv)==1):
        file="package.png"
    else:
        file = sys.argv[1]
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
    cv2.destroyWindow('image')
    cv2.destroyWindow("Live Feed")
    return 2
        
	

print("Press c to capture a Image")
#print(sys.argv[1])
while rval:
    cv2.imshow("Live Feed", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    b=0
    
    b =capture()
    if (b==2):
        break
    	
    	
    
		
cv2.destroyWindow("Live Feed")
