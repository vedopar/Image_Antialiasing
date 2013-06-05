Image_Antialiasing
==================
Environment for running the script:

Date: Spring Semester 2013 USC

Porject Info:
	This is the first project of csci576-Multimedia System Design.
	There are 3 apps in this project.
	Part 1 –Spatial Resampling and Aliasing
		Input an image of size 512x512 and create a resampled image
		with or without antialiasing.
		example:
			Mypart1.exe 16 2.0 0
			16 is the number of lines on the original image, 2.0 is
			the resampling factor,in this way the generated would be
			256x256. 0 is a boolean variable indicating not using anti
			aliasing,1 stands for using that function.
	Part 2 –TemporalAliasing
		Rotating the original image clockwisely at a certain specified 
		speed. The output video is also of size 512x512 but it will be 
		given an fps rate of display, which means it will be updated at 
		specific times.
		example:
			Mypart2.exe 64 4.0 10.0
			The first parameter n is the number of radial lines in original
			image.
			The second parameter s will be a speed of rotations in terms of
			rotations per second.
			The third parameter will be the fps value for the output.
	Part 3
		Change part2 to take in two additional parameters:
			The fourth parameter will be a boolean value (0 or 1) suggesting
			whether or not you want to deal with aliasing.
			The fifth parameter will be a scale factor that scales the input 
			video down by a factor.
		example:
			Mypart3.exe 64 4.0 7.0 1 2.0


Dependent Libs:
	part1:	
	  python 2.7.3
	  http://www.python.org/download/	
	  python PIL 1.1.7
	  http://www.pythonware.com/products/pil/	
	  you might need library Tkinter , ImageTk and math if there is none.
	
	part2&3:	
	  opencv 2.4.3
	  http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.3/	  
	  numpy 1.6.2
	  http://sourceforge.net/projects/numpy/files/NumPy/1.6.2/

Additional Info:
	for video part, I program to generate original.avi and output.avi video files
	instead of one single video file. 
	Also in order to test the temporal aliasing part, I add one more red
	line in the "wheel" which would help me to indicate the observed speed
	of the video more easily.
	way for temporal anti-aliasing:
	  I use the easiest way, which is to check the fps if it is greater than or equal 
	  to the Nyquist factor, which is 2 times the real speed. If not just change the 
	  fps to be greater than it.
	
	How to generate .exe file:	
	  need:
	    py2exe 0.6.9
	    http://sourceforge.net/projects/py2exe/files/py2exe/	
	  steps:
	    run command:
		python setup.py py2exe
	    there should be two directories generated
	    in the dist/ directory there should exist
	    the .exe file. 	
	
