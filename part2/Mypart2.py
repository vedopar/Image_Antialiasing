'''
Created on 2013-2-12

@author: vedopar
'''
import Image as Image
import ImageDraw
import sys
import math
import Tkinter
import ImageTk
import cv2
import cv2.cv as cv
    
fps=0
n=0
s=0
width=512
height=512
r=256
pi=math.pi
degree_value=0
img_name="source.png"

def getArgs():
    global n
    global s
    global fps
    try:
        fps=float(sys.argv[3])
        n=int(sys.argv[1])
        if n<=0 or n>360:
            print "n is out of range!!"
            return 1
        s=float(sys.argv[2])
        if s<=0:
            print "s is negative!"
            return 1
    except IOError as e:
        print "input format error!"
        return 1
    except IndexError as e:
        print "input format error!"
        return 1
    except ValueError as e:
        print "input format error!"
        return 1
    return 0

def drawImage(sd):
    global width
    global height
    global degree_value
    global pi
    global n
    global r
    global img_name
    im2=Image.new("RGB",(width,height),"white")
    draw=ImageDraw.Draw(im2)
    draw.ellipse((0, 0, 2*r, 2*r), fill=(255, 255, 255),outline=0)
    #draw.ellipse((width, 0, width+2*r, 2*r), fill=(255, 255, 255),outline=0)
    #r2=r+width
    for i in range(n):
        dv=i*degree_value+sd
        y=(int)(r*math.sin(dv)+r)
        x=(int)(r*math.cos(dv)+r)
        draw.line([(x,y),(r,r)],fill=0)
    draw.line([((int)(r*math.cos(sd/3)+r),(int)(r*math.sin(sd/3)+r)),(r,r)],fill=128)
    del draw
    return im2.save(img_name)

def main():
    global degree_value
    global pi
    global s
    global fps
    if getArgs()==1:
        return
    degree_value=2*pi/n
    #drawImage(0)
    #return
    writer=cv.CreateVideoWriter("original.avi", 0, 7*s, (width,height))
    writer2=cv.CreateVideoWriter("output.avi", 0, fps, (width,height))
    nFrames=int(14*s)
    addon=pi*2/7
    c=addon
    drawImage(0)
    for i in range(nFrames):
        c=c+addon
        drawImage(c)
        img2=cv.LoadImage(img_name)
        cv.WriteFrame(writer, img2)
        
    nFrames=int(2*fps)
    addon2=pi*2*s/fps
    c2=addon2
    drawImage(0)
    for j in range(nFrames):
        c2=c2+addon2
        drawImage(c2)
        img2=cv.LoadImage(img_name)
        cv.WriteFrame(writer2, img2)

    #cv2.ReleaseVideoWriter(writer)
    
if __name__ == '__main__':
    main()
