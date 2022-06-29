"""
This jython scripts illustrates a workflow with on-the-fly processing : acquired images are directly opened in Fiji as a hyperstack, using the "Make hyperstacks" plugins from ACQUIFER.
In a more realistic scenario, images could also be processed and not only viewed, for instance with the batch process hyperstack (macro) plugin.

The script performs the imaging of Z-stacks with 2 channels (brightfield and a fluo channel) for a few wells.
Before each acquisition a software autofocus is run using the brightfield channel.

REQUIREMENTS
- Fiji with the ACQUIFER update site activated
- running the script on a control PC/HIVE connected to the Imaging Machine
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
#@ File (label="Project directory", style="directory") project
#@ String (label="plate ID") plate_id
from ij import IJ
from acquifer.core        import TcpIp, WellPosition
from java.util.concurrent import TimeUnit

# Define our list of well with their coordinates
# these X,Y coordinates corresponds to the center of the well in mm
listWells = [WellPosition("A001", 14.335, 10.809),
			 WellPosition("A002", 23.370, 10.809),
			 WellPosition("A003", 32.404, 10.809)]

# Timelapse infos
nTimepoints = 3
timeStep    = 1 # minutes


def acquireStack():
	"""
	This custom utility function performs the Z-stack acquisition for both channels.
	It first runs a software autofocus using 2x2 binning then acquiring the images with full-resolution for the 2 channels
	IT is called for each well.
	"""
	
	# Define objective used for AF and acquisition
	# The objective index is between 1 and 4, with increasing magnifications
	# Typically the first objective (index 1) is the 2X
	objectiveIndex = 2
	
	## AUTOFOCUS
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
										50)    # zStepSize (micrometers)
	
	# Reset camera binning to full resolution before acquiring
	myIM.resetCamera()
	
	## ACQUISITION
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
	outputDir = myIM.acquireZstack(2,
								   objectiveIndex,
								   "100000", # use the 1st fluo light source, see the "LightSource" example script
								   1, 
								   70, 
								   120, 
								   zFocus,
								   nSlices, 
								   zStepSize)
	return outputDir

## START ACQUISITION
# Attempt connection to IM control software
try : 
	myIM = TcpIp() # open the communication port with the IM

except Error, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution


# Set project folder and plateID for output directory
# Images will be saved in a directory in the form projectFolder/timestamp_plateID
myIM.setDefaultProjectFolder(project.getPath())
myIM.setPlateId(plate_id)

# Set mode to script before starting the script to avoid switching between live/script
# Switching to script mode also defines the timestamp for the output directory
myIM.setMode("script")

for well in listWells:
	
	print "Imaging well :", well.getWellId() 
	
	myIM.moveXYto(well) # this update the well ID for metadata too
	outputDir = acquireStack()
	
	# ON-THE-FLY : Display the acquired images as a hyperstack in Fiji
	# This uses the macro-recorded command in jython of the ACQUIFER Make Hyperstack plugin, replacing the image directory and current well ID
	# NOTE : we need to convert from the upper case wellID ex: "A001" to a lower case version "a001"
	cmd = "directory=[{}] {} sub-position(s)=[] channel(s)=[] z-slice(s)=[] timepoint(s)=[] display_stack method=max start=1 stop=3 output_directory=[]".format(outputDir, well.ID.lower())
	IJ.run("Make hyperstacks", cmd);

myIM.closeConnection()
print "Done"