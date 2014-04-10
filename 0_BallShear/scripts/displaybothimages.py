import cv2
import math,sys
import numpy as np

if(len(sys.argv)!=3):
        print >> sys.stderr, 'Input arguments not found'
else:    
    orig = cv2.imread(sys.argv[1])
    img = cv2.imread(sys.argv[2])




    h, w = orig.shape[:2]
    vis = np.zeros((h, w*2+5), np.uint8)
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)
    vis[:h, :w] = orig
    vis[:h, w+5:w*2+5] = img

    cv2.imshow("image", vis)
    cv2.waitKey()
    cv2.destroyAllWindows()
