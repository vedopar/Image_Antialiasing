from PIL import Image,ImageDraw
import sys
import math
import Tkinter
import ImageTk

def main():
	is_antialiasing=0
	n=0
	s=0
	try:
		if int(sys.argv[3])>0:
			is_antialiasing=1
		n=int(sys.argv[1])
		if n<=0 or n>360:
			print "n is out of range!!"
			return
		s=float(sys.argv[2])
		if s<=0:
			print "s is negative!"
			return
	except IOError as e:
		print "input format error!"
		return
	except IndexError as e:
		print "input format error!"
		return
	except ValueError as e:
		print "input format error!"
		return
	width=512
	height=512
	im=Image.new("RGB",(width,height),"white")
	draw=ImageDraw.Draw(im)
	pi=math.pi
	tan_value=2*pi/n
	for i in range(n):
		tv=i*tan_value
		tn=math.tan(tv)
		x=0
		y=0
		if tv>=pi/4 and tv<pi*0.75:
			y=height
			x=(int)((y-height/2)/tn+width/2)
		elif tv>=1.25*pi and tv<1.75*pi:
			y=0
			x=(int)((y-height/2)/tn+width/2)
		elif tv>=0.75*pi and tv<1.25*pi:
			x=0
			y=(int)((x-width/2)*tn+height/2)
		else:
			x=width
			y=(int)((x-width/2)*tn+height/2)
		draw.line([(x,y),(width/2,height/2)],fill=0);
	del draw
	im2=None
	if is_antialiasing==1:
		im2=im.resize(((int)(width/s),(int)(height/s)),Image.ANTIALIAS)
	else:
		im2=im.resize(((int)(width/s),(int)(height/s)))
	root=Tkinter.Tk()
	tkim=ImageTk.PhotoImage(im)
	tkim2=ImageTk.PhotoImage(im2)
	l1=Tkinter.Label(root,image=tkim,anchor='w')
	l1.pack(side='left')
	l2=Tkinter.Label(root,image=tkim2,anchor='e')
	l2.pack(side='right')
	root.mainloop()

if __name__=="__main__":
	main()
