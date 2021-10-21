"""
This jython script demonstrates how to list image files from an Imaging Machine experiment directory.
A similar result can be obtained in the macro language, using the "Batch Process Images (macro)" plugin, and using in the text input the following commands

imagePath = getArgument(); // get image path for the current iteration
print(imagePath)

Back to jython, the code below uses the function getListImageFiles from acquifer.im04.FileUtils.
This function accepts optional filters in the form of lists, to return only image files for a specific well, subposition, channel, timepoint or Z-slice.
The list of files is then parsed to extract the metadata for each image file.

The script relies on the acquifer-core java package, provided with the acquifer update site.
This script can be run in the Fiji script editor, and requires a dataset of IM images.
Similar scripts in other scripting language can be written by adapting the import statements and general syntax.

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.core.im04 import FileUtils, Metadata
#from acquifer.core.im03 import FileUtils, Metadata # For an IM03 dataset, simply replace the import statment from the previous line with this line
from acquifer.ij.Utils import printArray # print each item of a list to a new line in the log window (more readable)
from ij import IJ

image_directory = image_directory.toString()

utils = FileUtils()
listFull = utils.getListImageFiles(image_directory) # without additional parameters, all IM image files are returned

IJ.log("\nList of image files")
printArray(listFull)

# Add filters for specific wells 
# If none, no filter is applied for the given dimension
listWell = ["B002"]
listSubpositions = None 
listChannel      = None
listZslice       = None
listTimepoint    = None

listFiltered = utils.getListImageFiles(image_directory, 
									   listWell, 
									   listSubpositions, 
									   listChannel, 
									   listZslice, 
									   listTimepoint)

IJ.log("\nWith dimension filter")
printArray(listFiltered)

# Parse the metadata for the list of image files that were filtered
listMetadatas = utils.getListMetadatas(listFiltered)

IJ.log("\nImages metadata")
printArray(listMetadatas)

# List wells actually present in the dataset
IJ.log("\nUnique wells")
printArray(Metadata.listUniqueWells(listMetadatas))