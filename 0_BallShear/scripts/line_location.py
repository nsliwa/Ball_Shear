from Tkinter import *
from tkFileDialog import askopenfilename
import Image, ImageTk,os,math
import numpy as np
if(len(sys.argv)<=3):
    print >> sys.stderr, 'Input Arguments are not correct. Please follow this templete analyzed  picture file location,virtual coordinate csv file location, physical coordinate csv location'

elif __name__ == "__main__":
    root = Tk()
    i=0
    x1=0
    x2=0
    y1=0
    y2=0
    dist=0
    #setting up a tkinter canvas with scrollbars
    frame = Frame(root, bd=3)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame,height=500,width=500, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)
    csv_virtual = open(sys.argv[2], 'r')
    csv_real = open(sys.argv[3], 'w')
    rOrigin_x = 0   
    rOrigin_y = 0


    #adding the image
    File = '../img/packageAnalyzed.png'
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    

    #function to be called when mouse is clicked
    def printcoords(event):
        global i,x1,x2,y1,y2,dist
        if(i==0):
            print (event.x,event.y)
            x1=event.x
            y1=event.y
        if(i==1):
            print (event.x,event.y)
            x2=event.x
            y2=event.y
            dist = math.hypot(x2 - x1, y2 - y1)
            print(dist)
            root.destroy()
            # Scaling
            vScale = dist
            rScale  = 5
            print "vScale:", vScale
            vOrigin_x = x1
            vOrigin_y = y1
            print "virtual: (" , vOrigin_x, ",", vOrigin_y, ")"

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
            i = 0
            vCoord = np.genfromtxt(csv_virtual, dtype=[('label', 'S5'), ('vCoord_x', 'i8'), ('vCoord_y', 'i8')], delimiter=",")
            print vCoord[0]
            for label, vX, vY in vCoord:
                rCoord_x = rOrigin_x+(vX - vOrigin_x) * conversionFactor
                rCoord_y = rOrigin_y+(vOrigin_y - vY) * conversionFactor

                if i > 0:
                    csv_real.write('\n')
                i=i+1
                csv_real.write(str(label)+','+str(rCoord_x)+','+str(rCoord_y));
        
                #csvwriter = csv.writer(csv_real, delimiter=',')
                #csvwriter.writerow([label, rCoord_x, rCoord_y])

                print "virtual: (" , vX, ",", vY, ")", "real: (" , rCoord_x, ",", rCoord_y, ")"
            
            csv_real.close()
            csv_virtual.close()
        i=i+1
        
            
            
    #mouseclick event
    canvas.bind("<Button 1>",printcoords)
    
    root.mainloop()
    
        
