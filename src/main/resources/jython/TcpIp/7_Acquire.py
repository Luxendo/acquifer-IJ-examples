"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This script demonstrates how to acquire images via the Java API from an external application. 
By default the acquire command is designed for the acquisition of Z-stacks. Single images can also be acquired by specifying the number of slice to 1.
For the acquire command, like for the autofocus command, the objective and camera settings are defined beforehand via the dedicated commands (see previous tutorial scripts).

The acquire commands can be called with an optional path argument to specify where the images should be saved.
If not specified, the images are saved in a subdirectory of the project directory.
The project directory can be defined using the command setDefaultProjectFolder or via the Imaging Machine software.
The images are saved in a subdirectory of the project directory, named using the user-defined PlateId and a unique timestamp.
Use setPlateId to define the plate id.

The images are named following the Imaging Machine naming syntax.
The values of the metadata tags in the filename can be updated using the set of setMetadata commands.
These commands should be called before the corresponding acquire command to update the well ID, subposition and timepoint tags.
Indeed contrary to running an experiment in the GUI, there is no way for the software to know what well, timepoint or subposition the next acquire command corresponds to.

NOTE about script/live mode
The acquire commands always switches the software to script mode.
If the software is in live mode before the acquire command is sent, the software will switch to script mode, acquire the images and return to live mode.
Switching between script and live mode takes a few seconds. Therefore for successive acquire commands, it is advised to switch to script mode once for all, before calling the acquire command,
using the setMode("script") command.

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
#@File (style="directory") directory

from acquifer.core import TcpIp
import os

try : 
	myIM = TcpIp() # open the communication port with the IM

except Error, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

directory = directory.getPath()

myIM.resetCamera() # use default setting, use setCamera functions to update ROI and/or binning

# Update metadata fields such as wellID, subposition (within a given well), timepoint
myIM.setMetadataWellId("A001") # this should be a 4-character string : a character and 3 digits 
myIM.setMetadataSubposition(1) # to specify if we are acquiring subpositions within a well
myIM.setMetadataTimepoint(1)   # for timelapse

# Define objective that we will pass to the acquire commands
# The objective index is between 1 and 4, with increasing magnifications
# Typically the first objective (index 1) is the 2X
objectiveIndex = 1

# OPTION1 : acquire with full set of arguments including custom directory to save the images
channelNumber = 1 # this is for filenaming (the CO tag)
lightSource = "brightfield"
detectionFilter = 2 # between 1 and 4
intensity = 50 # relative intensity of the lightsource in %
exposure = 100 # exposure in ms
zStackCenter = 18000 # in micrometers
nSlices = 20
zStepSize = 10 # micrometers
lightConstantOn = False

# For saveDirectory we pass a raw string (r prefix) so that backslashes are not interpreted as special characters
# one can also use normal string with double backslashes as separators \\ or forward slash /
# if the directory does not exist, it is automatically created
# if "" or None is passed as argument to acquire, the images are saved in the default project folder within a plate-specific directory (see below) 
saveDirectory = os.path.join(directory, "customDirectory")
outputDir = myIM.acquireZstack(channelNumber,
							   objectiveIndex, 
							   lightSource, 
							   detectionFilter, 
							   intensity, 
							   exposure, 
							   zStackCenter,
							   nSlices, 
							   zStepSize, 
							   lightConstantOn, 
							   saveDirectory)

print "Saved images in :", saveDirectory # which is also the same than outputDirectory in this case


# OPTION2 : Using default project folder and plate ID
# This avoids the need to specify the image directory for every new acquire command
#
# This will assure the following acquire commands are saved in the same subdirectory
# Indeed when switching to script mode, a timestamp is created that is used as part of the plate directory
projectDir = os.path.join(directory, "defaultProjectDirectory" )
myIM.setDefaultProjectFolder(projectDir)
myIM.setPlateId("myPlate")

# Switch to script mode before calling successive acquire commands
# otherwise each acquire command will switch back to live mode after execution (time consuming)
myIM.setMode("script")


# Define channel settings
detectionFilter = 2 # here we use the same detection filter between brightfield and fluo bu we could use different ones for each

intensityBF = 50  # relative intensity of the lightsource in %
exposureBF  = 100 # exposure in ms

intensityFluo = 80  # relative intensity of the lightsource in %
exposureFluo  = 150 # exposure in ms

# Stack settings (identical for brigtfield and fluo)
zStackCenter = 18000 # in micrometers
nSlices = 20
zStepSize = 10 # micrometers

# Acquire brightfield channel
# here we dont specify the output directory, so images will be saved in the default projectDirectory/timestamp_plateID
# The exact path of the output directory is returned by the command 
# lightConstantOn is not specified neither and default to False
myIM.setMetadataWellId("A001")
outDirectory = myIM.acquireZstack(1, # here we set channel number for brightfield to 1, this defines the value for the tag "CO" in the filename
								objectiveIndex,
								"brightfield", 
								detectionFilter,
								intensityBF, 
								exposureBF, 
								zStackCenter, 
								nSlices, 
								zStepSize) 

# Acquire fluo channel
outDirectory = myIM.acquireZstack(2, # here we set channel number for this fluo channel to 2, this defines the value for the tag "CO" in the filename
								objectiveIndex,
								"100000", # use the 1st fluo light source, see the "LightSource" example script
								detectionFilter, 
								intensityFluo, 
								exposureFluo, 
								zStackCenter,
								nSlices, 
								zStepSize,
								True, # here we specifiy lightConstantOn to true, so fluo light source is not blinking 
								None) # set the saveDirectory to None, in this case the images are saved to the default project directory as above

print "Saved images in :", outDirectory

myIM.closeConnection() # closing the connection will automatically switch back to live mode
print "Done"