"""
Generate a VirtualPlate and display it, from an IM directory.
The IM directory is expected to contain a dataset with a SINGLE SUBPOSITION
"""

#@ File (label="Select an IM directory", style="directory") image_directory
from acquifer.core.im04 import FileUtils, Metadata
from acquifer.ij.Utils  import printArray
from acquifer.ij        import VirtualPlate
from acquifer.core.im   import Plate
from ij import IJ, ImagePlus

image_directory = image_directory.toString()

listMetadata = FileUtils().getListMetadatas(image_directory) # list IM files and parse dimensions metadatas
sortedMetadata = Metadata.sortCopy(listMetadata, VirtualPlate.SORT_CZT) 
printArray(sortedMetadata)

layout = Plate.Wells96
downScaling = 10


# Method 1 - Create a VirtualPlate then wrap it into an ImagePlus
virtualPlate = VirtualPlate(listMetadata, layout, downScaling)
virtualPlate.deleteSlice(1) # to test

virtualPlateImp = ImagePlus("Method1 - After removing slice 1", virtualPlate)
virtualPlateImp.show() 

# Method 2 : directly create a hyperstack
plateStack = VirtualPlate.createHyperstackFromDataset(listMetadata,
													  layout,
													  downScaling)
imp2 = plateStack.toHyperstack()
imp2.show() 