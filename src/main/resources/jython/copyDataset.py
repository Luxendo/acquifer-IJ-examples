"""
This script demonstrates how to copy a full IM dataset, or only specific wells, subposition, channels...
"""
#@ File (label="Dataset directory", style="directory") src
#@ File (label="Target directory", style="directory") dst
from acquifer.core.im04 import FileUtils
import os

src = src.getPath()
dst = dst.getPath()

## Option 1 : Copy full dataset
copySubDirectories = True
dst1 = os.path.join(dst, "fullDataset")
FileUtils.copyDirectory(src, dst1, copySubDirectories) # this is a static method (same for all IM versions), ie we dont need to create an instance


## Option2 : Copy only a fraction of dataset according to following filters
# Leave a filter empty to take all available elements for this dimension
listWells      = []
listPositions  = []
listChannels   = [6]
listZ          = [3]
listTimepoints = [] 

# Create an instance of FileUtils (here specific to IM04)
fileUtils = FileUtils()
dst2 = os.path.join(dst, "subDataset")
copyLog = False
fileUtils.copyDataset(src, dst2, copyLog, listWells, 
									      listPositions,
										  listChannels,
			                              listZ,
										  listTimepoints)