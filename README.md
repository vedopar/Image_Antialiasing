Image_Antialiasing
==================
Environment for running the script:

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

note:
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