"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This is an example of realistic experiment running a timelapse acquisition from Fiji in the jython scripting language.
It performs the imaging of Z-stacks with 2 channels (brightfield and a fluo channel) for multiple wells and subpositions within wells.
Before each acquisition a software autofocus is run.

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
#@ File (label="Project directory", style="directory") project
#@ String (label="plate ID") plate_id

from acquifer.core        import TcpIp, WellPosition
from java.util.concurrent import TimeUnit
import collections

Well = collections.namedtuple('Well', ['ID', 'X', 'Y']) # Well here is like a constructor

# Define our list of well with their coordinates
# these X,Y coordinates corresponds to the center of the well in mm
listWell = [WellPosition("A001", 14.335, 10.809),
			WellPosition("A002", 23.370, 10.809),
			WellPosition("A003", 32.404, 10.809)]

# Timelapse infos
nTimepoints = 3
timeStep    = 1 # minutes


def acquireStack(subposition, timepoint):
	"""
	This custom utility function performs the Z-stack acquisition for both channels.
	It first runs a software autofocus using 2x2 binning then acquiring the images with full-resolution for the 2 channels
	It is called at each timepoint for each subposition.
	"""
	
	# First update metadata
	#myIM.setMetadataWellId(wellID) # not needed when using moveXYto(well), automatically updated
	myIM.setMetadataSubposition(subposition)
	myIM.setMetadataTimepoint(timepoint)
	
	# Define objective used for AF and acquisition
	# The objective index is between 1 and 4, with increasing magnifications
	# Typically the first objective (index 1) is the 2X
	objectiveIndex = 2
	
	# Run the autofocus using the brightfield channel and 2x2 binning
	myIM.setCameraBinning(2)
	zCenter = 19000 # for AF only, in micrometers 
	zFocus = myIM.runSoftwareAutoFocus(objectiveIndex,
										"bf",   # lightSource
										2,     # detectionFilter 
										80,    # intensity (%)
										50,    # exposure (ms)
										zCenter, # zStackCenter (micrometers)
										11,    # nSlices 
										15)    # zStepSize (micrometers)
	
	# Reset camera binning to full resolution before acquiring
	myIM.resetCamera()
	
	# Define common Z-stack parameters for both channels
	# Important that both Z-stack have identical dimensions for both channels
	# otherwise not possible to overlay the 2 channels ! 
	nSlices = 21
	zStepSize = 10 # micrometers
	
	# Acquire 1st channel : brightfield
	myIM.acquireZstack(1, # channel number, for filenaming : tag "CO"
						 objectiveIndex,
						 "brightfield", # lightSource
						 2,             # detectionFilter
						 80,            # intensity (%) 
						 100,           # exposure (ms)
						 zFocus,        # z-stack center 
						 nSlices, 
						 zStepSize)
	
	# Acquire fluo channel
	myIM.acquireZstack(2,
						 objectiveIndex,
						 "100000", # use the 1st fluo light source, see the "LightSource" example script
						 3, 
						 70, 
						 120, 
						 zFocus,
						 nSlices, 
						 zStepSize)


# Start connection
try : 
	myIM = TcpIp() # open the communication port with the IM

except Exception, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution


# Set output directory
myIM.setDefaultProjectFolder(project.getPath())
myIM.setPlateId(plate_id)

# Set mode to script before starting the script to avoid switching between live/script
myIM.setMode("script")

for timepoint in range(1, nTimepoints+1): # range is exclusive ie it will be from 1 to 3
	
	# Wait before next timepoint
	if timepoint != 1: # does not wait for the ´first iteration
		print "Waiting for", timeStep, "minutes"
		TimeUnit.MINUTES.sleep(timeStep)
		#TimeUnit.HOURS.sleep(timeStep) # use this one for hours
	
	print "Starting timepoint :", timepoint
	
	for well in listWell:
		
		print "Imaging well :", well.getWellId()
		myIM.moveXYto(well) # this command also updates the current wellId for filenames, no need to call setMetadataWellId
		
		# Acquire 1st subposition
		acquireStack(1, timepoint) # acquireStack(subPosition, timepoint)
		
		# Acquire 2nd subposition which is 2.5 mm apart from the center in X and Y
		myIM.moveXYby(2.5, 2.5)
		acquireStack(2, timepoint)


myIM.closeConnection()
print "Done"