"""
This snippet demonstrates the use of the Dataset object, which represents a view of an IM experiment directory. 
A Dataset is a fixed view of an IM directory : depending on optional dimension filters it may not represent the full image directory. 
To create a dataset, one uses a DatasetBuilder, which provides a convenient syntax for optional dimensions filtering and sorting. 
The dataset is recovered from the Builder by calling the method build. 
Image files in a Dataset are represented as ImagePlane. 
"""
#@ File (label="Select an IM directory", style="directory") directory 
from ij import IJ 
from acquifer.ij import Utils 
from acquifer.core.im.ImagePlane import SortOrder 
from acquifer.core.im04          import DatasetBuilder 
#from acquifer.core.im03 import DatasetBuilder # uncomment for IM03 
 
# We create an instance of DatasetBuilder 
# We will use it, in different ways then  
builder = DatasetBuilder(directory)  
 
 
#### Unfiltered and unsorted dataset, get all images in the directory ### 
dataset = builder.build() # you could also directly do DatasetBuilder(directory).build() of course  
print dataset 
 
 
 
 
##### Dataset sorting #### 
# The sort order defines how the images (ie the corresponding ImagePlane) are sorted in the dataset 
# This can be achieved by adding the sortBy(sortOrder) to the builder call 
print "List of possible sort orders:" 
for order in SortOrder().getClass().getFields(): # You dont need to create a SortOrder in practice, here just to access the fields names 
	print order.getName() 
 
sortOrder = SortOrder.SORT_TZC # Time, Z-slice and channel, in the final list, the channels will vary first, then Z then T 
 
dataset   = builder.sortBy(sortOrder)\
				   .build() 
 

listPlanes = dataset.getListOfImagePlanes()                          # get the list of images (ImagePlane objects) in this dataset instance
print "\nFirst 2 ImagePlanes in sorted dataset : ", listPlanes[:2] # show only the first 2 ImagePlane below in the command line output
IJ.log("\nSorted dataset")                                        
Utils.printArray(listPlanes)                                       # show the full list in a log window
 
 

#### Dataset with dimensions filtering ##### 
# We can also build a dataset containing only images matching some dimensions of interest 
dataset = builder.includeWellIds(["A001", "B001"])\
				 .includeZ([1,2,3])\
				 .build() 
 
print "\nDataset including only specific Wells and Z-positions", dataset