"""
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
"""
from acquifer.core import TcpIp
from java.lang import Thread

myIM = TcpIp()

myIM.setObjective(1)
myIM.resetCamera() # use default setting, use setCamera functions to update ROI and/or binning

# Update metadata fields such as wellID, subposition (within a given well), timepoint
myIM.setMetadataWellId("C002") # this should be a 4-character string : a character and 3 digits 
myIM.setMetadataSubposition(1) # to specify if we are acquiring subpositions within a well
myIM.setMetadataTimepoint(1)   # for timelapse

# OPTION1 : Full set of arguments including custom directory to save the images
channelNumber = 1 # this is for filenaming (the CO tag)
lightSource = "brightfield"
detectionFilter = 2 # between 1 and 4
intensity = 50 # relative intensity of the lightsource in %
exposure = 100 # exposure in ms
zStackCenter = 18000 # in µm
nSlices = 20
zStepSize = 10 # µm
lightConstantOn = False

# For saveDirectory we pass a raw string (r prefix) so that backslashes are not interpreted as special characters
# one can also use nromal string with double backslashes as separators \\ or forward slash /
# if the directory does not exist, it is automatically created
saveDirectory = r"C:\Users\Default\Desktop\MyDataset" 

myIM.acquire(channelNumber, 
			 lightSource, 
			 detectionFilter, 
			 intensity, 
			 exposure, 
			 zStackCenter,
			 nSlices, 
			 zStepSize, 
			 lightConstantOn, 
			 saveDirectory)


# OPTION2 : Using default project folder and plate ID
myIM.setDefaultProjectFolder(r"C:\Users\Default\Desktop\MyDataset")
myIM.setPlateId("test") # every new call to acquire will save the images in a new sub-folder of default project folder, named with a unique timestamp followed by the plateID

myIM.setMetadatWellId("A001")
myIM.acquire( channelNumber, 
			 lightSource, 
			 detectionFilter, 
			 intensity, 
			 exposure, 
			 zStackCenter,
			 nSlices, 
			 zStepSize) # here we dont specify the output directory nor the lightConstantOn which default to False

myIM.setMetadatWellId("A002")
myIM.acquire( channelNumber, 
			 lightSource, 
			 detectionFilter, 
			 intensity, 
			 exposure, 
			 zStackCenter,
			 nSlices, 
			 zStepSize,
			 True,
			 None) # here we specify lightConstantOn to True, and set the saveDirectory to None, in this case the images are also saved to the default project directory within a plate subdirectory

myIM.closeConnection()