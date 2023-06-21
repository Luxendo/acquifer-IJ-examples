"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This script demonstrates how to adjust camera settings via the java API for external control of the IM.
In live mode, updating the camera parameters is directly reflected in the image-preview in the Imaging Machine software.
The camera settings are typically set once and will apply for following commands acquire, runSoftwareAutofocus... 

2 parameters can be changed for the camera : 

- the size of the field of view (sensor area)
this can be used to image specific regions of interest, thus reducing the image size and the overall dataset size
The default area is the full sensor area which corresponds to 2048 x 2048 pixels.
The area is specified as a tuple of 4 values (x,y,width,height) with x,y the coordinates of the top left pixel of the effective area (default to x=0, y=0).
These coordinates are always specified in "full-resolution coordinates", even if binning is used. 

- the binning factor
With binning, neighboring pixels are grouped together (1:no binning, 2:2x2 or 4:4x4).
This results in larger pixels, hence reducing image-resolution, but also reducing image size and again the size of the overall dataset.
Besides, using binning, the brightness of the grouped pixels are combined, therefore one can reduce light intensity and/or exposure to achieve a similar brightness
than the original full resolution image.

The exposure time of the camera is set for each channel separately, with one of the following commands : setBrightfield, setFluoChannel or setLightSource.

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
from acquifer.core import TcpIp
from java.lang import Thread

try : 
	myIM = TcpIp() # open the communication port with the IM

except Exception, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

# Switch on the brightfield channel to activate an image-preview in the IM software
myIM.setBrightField(1, 2, 50, 100)


# You have different options to set the camera sensor area an/or binning

# OPTION 1 : Set the camera sensor area + binning all at once
x = 200
y = 200
width = 1024
height = 1024
binning = 2
myIM.setCamera(x, y, width, height, binning)
Thread.sleep(5000) # wait 5 secs, to leave the opportunity to see it


## OPTION 2 : Set the camera sensor area only, 
myIM.setCamera(x, y, width, height)
Thread.sleep(5000) # wait 5 secs, to leave the opportunity to see it


# OPTION 3 : Set the binning factor only
# binning value can be one of 1 (no binning), 2 (2x2), 4 (4x4)
myIM.setCameraBinning(binning)
Thread.sleep(5000) # wait 5 secs, to leave the opportunity to see it


# Use resetCamera to re-establish the sensor area to full resolution (2048 x 2048) and no binning (value of 1)
myIM.resetCamera()

myIM.closeConnection()