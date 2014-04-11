#!/usr/bin/env python
'''
mouse_and_match.py [-i path | --input path: default ./]

Demonstrate using a mouse to interact with an image:
 Read in the images in a directory one by one
 Allow the user to select parts of an image with a mouse
 When they let go of the mouse, it correlates (using matchTemplate) that patch with the image.
 ESC to exit
'''
import numpy as np
import cv2

# built-in modules
import os.path
import sys
import glob
import mmap
import argparse
import csv
from math import *
#from matplotlib import pyplot as plt

drag_start = None
sel = (0,0,0,0)
i=0
result=0
loc=0
points=[]
x1=[]
y1=[]

def onmouse(event, x, y, flags, param):
    global drag_start, sel,i,result,loc,label,x1,y1,points
    if event == cv2.EVENT_LBUTTONDOWN:
        drag_start = x, y
        sel = 0,0,0,0
    elif event == cv2.EVENT_LBUTTONUP:
        if sel[2] > sel[0] and sel[3] > sel[1]:
            patch = gray[sel[1]:sel[3],sel[0]:sel[2]]
            result = cv2.matchTemplate(gray,patch,cv2.TM_CCOEFF_NORMED)
            result = np.abs(result)**3
            res=result
            w, h = patch.shape[::-1]
            threshold = .8
            loc = np.where( res >= threshold)
            img_rgb=cv2.imread(sys.argv[1],1)
            
            font = cv2.FONT_HERSHEY_PLAIN
            lastpt1 =0
            lastpt2 =0
            lastpt3=0
            if(len(sys.argv)<=2):
                text_file = open("coordinate.csv", "w")
            else:
                text_file = open(sys.argv[2], "w")
            difference2=0
            pt1=[]
            pt2=[]
            
            for pt in zip(*loc[::-1]):
                #if( abs(lastpt1-(pt[0]+w/2))>0):
                    difference = abs(lastpt1 -(pt[0]+w/2))   
                    
                    difference2 = abs(lastpt2 -(pt[0]+w/2))
                    if(difference > w/2 and difference2 > w/2):
                        
                        #difference2 = abs(lastpt3-(pt[0]+w/2))
                        #if(difference2 >5):
                        if(((pt1.count(pt[0]+w/2) ==0) or pt2.count(pt[1]+h/2)==0)and((pt1.count(1+pt[0]+w/2) ==0) or pt2.count(1+pt[1]+h/2)==0) and ((pt1.count(pt[0]+w/2) ==0) or pt2.count(1+pt[1]+h/2)==0) and ((pt1.count(1+pt[0]+w/2) ==0) or pt2.count(pt[1]+h/2)==0)):
                                #if i > 0:
                                #    text_file.write('\n')
                                i=i+1
                                #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
                                #cv2.circle(img_rgb,(pt[0]+w/2,pt[1]+h/2),1,(0,0,120),3) # draw the center of the circle
                                #print((pt[0]+w/2,pt[1]+h/2),i  ,difference)
                                #text_file.write(str(i)+','+str(pt[0]+w/2)+','+str(pt[1]+h/2));
                                #cv2.putText(img_rgb,str(i),(pt[0]+w/4,pt[1]+h), font,1,(100,100,255),1,cv2.CV_AA)
                                lastpt2= lastpt1
                                lastpt1= pt[0]+w/2
                                
                                bb=0
                                xmin=(pt[0]+w/2) -w
                                xmax=(pt[0]+w/2) +w
                                ymin=(pt[1]+h/2) -h
                                ymax=(pt[1]+h/2) +h
                                for k in range(1, len(points)):
                                    if(points[k][1]>xmin and points[k][1]<xmax):
                                        if(points[k][2]>ymin and points[k][2]<ymax):
                                            bb=1
                                        


                                if(bb==0):
                                    points.insert(i,(i,pt[0]+w/2,pt[1]+h/2))
                                
                    pt1.append(pt[0]+w/2)
                    pt2.append(pt[1]+h/2)

            #print label[3][0]
            points.sort()
            print points
            aa=0
            for j in range(0, len(points)):
                #xmin =(points[j][1])-w
                #xmax = (points[j][1])+w
                #ymin =(points[j][2])-h
                #ymax = (points[j][2])+h
                #for k in range (2, len(points)):
                    
                    #if((points[j][1])-(points[k][1])<2):
                       #if(abs((points[j][2])-(points[k][2]))<2):
                    #       aa=1
                       
                   #     if(ymin<points[k][2]<ymax):
                   #        aa=1
                    #if((range(points[k][1],w) in points[j])and (range(points[k][2],h) in points[j])):
                    #    aa=1
                    #if((range(points[k][1],-w) in points[j])and (range(points[k][2],-h) in points[j])):
                    #    aa=1
                    #if((range(points[k][2],h) in points[j])):
                    #    aa=1
                    #if((range(points[k][2],-h) in points[j])):
                    #    aa=1
            #if(aa==0):
                #if j > 0:
                #    text_file.write('\n')
                cv2.circle(img_rgb,((points[j][1]),(points[j][2])),1,(0,0,120),3) # draw the center of the circle
                cv2.putText(img_rgb,str(points[j][0]),(points[j][1]-w/4,points[j][2]+h/2), font,1,(100,100,255),1,cv2.CV_AA)    
                
                text_file.write(str(points[j][0])+','+str(points[j][1])+','+str(points[j][2]));         
                if j >= 0:
                    text_file.write('\n')
            val, result = cv2.threshold(result, 0.01, 0, cv2.THRESH_TOZERO)
            result8 = cv2.normalize(result,None,0,255,cv2.NORM_MINMAX,cv2.CV_8U)
            if(len(sys.argv)<=3):
                cv2.imwrite('res.png',img_rgb)
                cv2.imshow("res.png", img_rgb)
            else:
                cv2.imwrite(sys.argv[3],img_rgb)
                #plt.imshow(img_rgb)
                #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
                #plt.show()
                cv2.imshow(sys.argv[3], img_rgb)
            
        drag_start = None
    elif drag_start:
        #print flags
        if flags & cv2.EVENT_FLAG_LBUTTON:
            minpos = min(drag_start[0], x), min(drag_start[1], y)
            maxpos = max(drag_start[0], x), max(drag_start[1], y)
            sel = minpos[0], minpos[1], maxpos[0], maxpos[1]
            img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(img, (sel[0], sel[1]), (sel[2], sel[3]), (0,255,255), 1)
            cv2.imshow("gray", img)
        else:
            print "selection is complete"
            drag_start = None

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Demonstrate mouse interaction with images')
    #parser.add_argument("-i","--input", default='./', help="Input directory.")
    #args = parser.parse_args()
    #path = args.input

    cv2.namedWindow("gray",1)
    cv2.setMouseCallback("gray", onmouse)
    '''Loop through all the images in the directory'''
    #for infile in glob.glob( os.path.join(path, '*.*') ):
        #ext = os.path.splitext(infile)[1][1:] #get the filename extenstion
    #if ext == "png" or ext == "jpg" or ext == "bmp" or ext == "tiff" or ext == "pbm":
            #print infile
    if(len(sys.argv)<=3):
        print >> sys.stderr, 'Input Arguments are not correct. Please follow this templete input picture file location,output csv file location, output image file location'
        #infile="package1.png"
        cv2.destroyAllWindows()
    else:
        infile = sys.argv[1]
        if(os.path.exists(sys.argv[1])):
            img=cv2.imread(infile,1)
            #if img == None:
                #continue
            sel = (0,0,0,0)
            drag_start = None
            gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray",gray)
            #plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
            #plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
            #plt.show()
        else:
            cv2.destroyAllWindows()
            print >> sys.stderr, 'Input Arguments are not correct. Please follow this templete input picture file location,output csv file location, output image file location'

        if (cv2.waitKey() & 255) == 27:
            #break
            cv2.destroyAllWindows()
