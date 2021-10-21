"""
Once images from a directory are listed, and metadata extracted, one can sort the list of images in a custom order of dimensions.
The default sorting order is as following (well, subposition, timepoint, Z-slice, -channel).
-channel means that the channels are sorted in reverse order, ie channel 6 (Brightfield) first.

This script takes an image directory and returns the list of IM image files first unsorted and then sorted using the default order.

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.core.im04 import FileUtils, Metadata
#from acquifer.core.im03 import FileUtils, MetadataParser, Metadata # For an IM03 dataset, simply replace the import statement from the previous line with this line
from acquifer.ij.Utils import printArray # print each item of a list to a new line in the log window (more readable)

from java.util        import Collections 
from ij               import IJ

image_directory = image_directory.toString()

utils = FileUtils()

# Get Metadata
listMetadatas = utils.getListMetadatas(image_directory)

IJ.log("\nImages metadata (unsorted)")
printArray(listMetadatas)

# Sort list of metadatas in the following order (well, subposition, timepoint, Z-slice, -channel), for channels reversed (CO6: Brightfield first)

# Sort the list and store it in a new list (ie duplicated the data)
sortedMetadatas = Metadata.sortCopy(listMetadatas)

# Or sort the list in place
Metadata.sort(listMetadatas)
# equivalent to
# Collections.sort(listMetadatas, Metadata.defaultOrder)
# listMetadatas is initially a java ArrayList, which also has a .sort(Comparator) method, but in jython, it is overwritten by the .sort(callable) method


IJ.log("Sorted copy == in-place sorted list :" + str(sortedMetadatas == listMetadatas))
IJ.log("\nImages metadata (sorted)")
printArray(sortedMetadatas)
print "See log window"