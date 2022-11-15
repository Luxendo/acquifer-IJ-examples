#@ File (label="Select an IM directory", style="directory") directory
from acquifer.core import Dataset
from acquifer.core.im04 import ImagePlane, DatasetBuilder
from acquifer.core.im.ImagePlane import SortOrder

from acquifer.ij import Utils 
from ij import IJ

# Unfiltered and unsorted dataset, get all images
dataset1 = DatasetBuilder(directory).build()

#dataset = Dataset(builder)
print "Dataset unfiltered", dataset1



## WITH DIMENSIONS FILTER
#filterWells        = ["A001","A002"]
filterWells       = [] # empty list as filter should return all wells
filterSubPositions = []
filterChannels     = []
filterZ            = []
filterTimepoints   = [1,2]

# Define custom sorting
#sortOrder = None
#sortOrder = SortOrder.SORT_WELL
#sortOrder = SortOrder.SORT_SUBPOSITION
#sortOrder = SortOrder.SORT_CHANNEL
#sortOrder = SortOrder.SORT_Z
#sortOrder = SortOrder.SORT_TIMEPOINT
sortOrder = SortOrder.SORT_WELL_SUBPOSITION_TZC

# Unfiltered and unsorted dataset, get all images
# Use backslashes \ to spread the command on multiple lines
dataset2 = DatasetBuilder(directory).includeWellIds(filterWells) \
									.includeSubpositions(filterSubPositions) \
								    .includeChannels(filterChannels) \
								    .includeZ(filterZ) \
								    .includeTimepoints(filterTimepoints) \
								    .sortBy(sortOrder) \
								    .build()

#dataset = Dataset(builder)
print "Dataset filtered", dataset2
IJ.log("\nlist of images")
Utils.printArray(dataset2.getListOfImagePlanes())