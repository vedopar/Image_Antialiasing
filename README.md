Image_Antialiasing
==================
<p>
Date: Spring Semester 2013 USC
</p>
<p>
Porject Info:<br/>
	This is the first project of csci576-Multimedia System Design.<br/>
	There are 3 apps in this project.<br/>
	Part 1 –Spatial Resampling and Aliasing<br/>
		Input an image of size 512x512 and create a resampled image<br/>
		with or without antialiasing.<br/>
		example:<br/>
			Mypart1.exe 16 2.0 0<br/>
			16 is the number of lines on the original image, 2.0 is<br/>
			the resampling factor,in this way the generated would be<br/>
			256x256. 0 is a boolean variable indicating not using anti<br/>
			aliasing,1 stands for using that function.<br/><br/>
	Part 2 –TemporalAliasing<br/>
		Rotating the original image clockwisely at a certain specified <br/>
		speed. The output video is also of size 512x512 but it will be <br/>
		given an fps rate of display, which means it will be updated at <br/>
		specific times.<br/>
		example:<br/>
			Mypart2.exe 64 4.0 10.0<br/>
			The first parameter n is the number of radial lines in original
			image.<br/>
			The second parameter s will be a speed of rotations in terms of
			rotations per second.<br/>
			The third parameter will be the fps value for the output.<br/><br/>
	Part 3<br/>
		Change part2 to take in two additional parameters:<br/>
			The fourth parameter will be a boolean value (0 or 1) suggesting<br/>
			whether or not you want to deal with aliasing.<br/>
			The fifth parameter will be a scale factor that scales the input <br/>
			video down by a factor.<br/>
		example:<br/>
			Mypart3.exe 64 4.0 7.0 1 2.0<br/>

</p>
<p>
Dependent Libs:<br/>
	part1:	<br/>
	  python 2.7.3<br/>
	  http://www.python.org/download/<br/>	
	  python PIL 1.1.7<br/>
	  http://www.pythonware.com/products/pil/<br/>	
	  you might need library Tkinter , ImageTk and math if there is none.<br/><br/>
	
	part2&3:<br/>	
	  opencv 2.4.3<br/>
	  http://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.4.3/	  <br/>
	  numpy 1.6.2<br/>
	  http://sourceforge.net/projects/numpy/files/NumPy/1.6.2/<br/>
</p>
<p>
Additional Info:<br/>
	for video part, I program to generate original.avi and output.avi video files<br/>
	instead of one single video file. <br/>
	Also in order to test the temporal aliasing part, I add one more red<br/>
	line in the "wheel" which would help me to indicate the observed speed<br/>
	of the video more easily.<br/>
	way for temporal anti-aliasing:<br/>
	  I use the easiest way, which is to check the fps if it is greater than or equal <br/>
	  to the Nyquist factor, which is 2 times the real speed. If not just change the <br/>
	  fps to be greater than it.<br/>
	<br/>
	How to generate .exe file:<br/>	
	  need:<br/>
	    py2exe 0.6.9<br/>
	    http://sourceforge.net/projects/py2exe/files/py2exe/<br/>	
	  steps:<br/>
	    run command:<br/>
		python setup.py py2exe<br/>
	    there should be two directories generated<br/>
	    in the dist/ directory there should exist
	    the .exe file. 	<br/>
</p>	
