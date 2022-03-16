"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This script demonstrate how to run autofocus via an external application like python.
The runHardwareAutofocus / runSoftwareAutofocus commands can be called both in "live" and "script" mode.

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
from acquifer.core import TcpIp
from java.lang import Thread

try : 
	myIM = TcpIp() # open the communication port with the IM

except Error, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

# SOFTWARE AUTOFOCUS
"""
Software autofocus is run with the current camera settings.
To use different camera settings (ROI acquisition or binning), you would need to first call one of these functions
myIM.setCamera(x, y, width, height, binning)
myIM.setCamera(x, y, width, height) # with default binning of 1
myIM.setCameraBinning(factor)
"""


objective = 1      # Objective index, 1 is usually 2X
lightSource = "bf" # as in setLightSource, here using brightfield, for fluo use a 6-digit code such as "001000" as in setFluoChannel 
detectionFilter = 2
intensity = 80
exposure = 100
zStackCenter = 18000 # center of the stack (in micrometers) imaged to evaluate the focus
nSlices = 11         # this means we measure the focus for 5 slices above and 5 below the center slice -> 5 + 1 (center) + 5 = 11
zStepSize = 10       # distance in micrometers between slices in the "autofocus stack"

"""
you might want to check the light parameters using setLight before running the autofocus to make sure the parameters allow to distinguish something from the image 
The search range along the Z-axis is always (nSlices - 1) x zStepSize
Here 11 slices x 10 makes 110 micrometers
"""

print "Starting software autofocus, focus value will be printed once the focus search is done."
zFocus = myIM.runSoftwareAutoFocus(objective,
									lightSource, 
									detectionFilter, 
									intensity, 
									exposure, 
									zStackCenter,
									nSlices, 
									zStepSize)

print "Z-Focus = {} micrometers".format(zFocus)




# HARDWARE AUTOFOCUS
# Hardware autofocus use its own light source and detector so you dont need to choose an intensity/exposure
# You only have to choose the objective, detectionFilter and starting Z position
print "Starting hardware autofocus, focus value will be printed once the focus search is done."
objective = 1
detectionFilter = 1
zStart = 18500 # starting Z-coordinate for the autofocus search, in micrometers

zFocus = myIM.runHardwareAutoFocus(objective, detectionFilter, zStart)

print "Z-Focus = {} micrometers".format(zFocus)