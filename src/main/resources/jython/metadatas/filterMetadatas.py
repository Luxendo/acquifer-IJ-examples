"""
This jython script demonstrates how to list images and their dimension-metadatas from a directory of images.
The list of images and metadatas (actually a list of Metadata objects) is then filtered to keep only specific dimensions.
It also shows how to recover the set of unique wells present in a list of Metadata objects

The script relies on the acquifer-core java package, provided with the acquifer update site.
This script can be run in the Fiji script editor, and requires a dataset of IM images.
Similar scripts in other scripting language can be written by adapting the import statements and general syntax.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
#@ File (label="Select an IM directory", style="directory") image_directory

from acquifer.core.im04 import FileUtils, Metadata
#from acquifer.core.im03 import FileUtils, Metadata # For an IM03 dataset, simply replace the import statment from the previous line with this line
from acquifer.ij.Utils  import printArray
from ij import IJ

image_directory = image_directory.toString()

utils = FileUtils()
listFull = utils.getListMetadatas(image_directory) # list IM files and parse dimensions metadatas

# Original list of metadata
print "\nUnfiltered list"
print len(listFull), "images"
print "Wells : ", Metadata.listUniqueWells(listFull) 



# Option 1 : Filter by well position
print "\nFilter by well position"

filterWells        = ["B001","B002"]
#filterWells        = [] # empty list as filter should return all wells

filteredByWell = Metadata.filterWells(listFull, filterWells)
print len(filteredByWell), " images"
print "Wells: ", Metadata.listUniqueWells(filteredByWell) 



# Option 2: Filterwith mulitple dimensions
print "\nFilter by with multiple dimensions"
# for wells use the same as above
filterSubPositions = []
filterChannels     = []
filterZslices      = [1]
filterTimepoints   = []

filteredMultiDimension = Metadata.filter(listFull,
										  filterWells,
										  filterSubPositions,
										  filterChannels,     
										  filterZslices,      
										  filterTimepoints)
										  
print len(filteredMultiDimension), " images"
print "Wells: ", Metadata.listUniqueWells(filteredMultiDimension)

print "See log window for list of filtered metadatas"
printArray(filteredMultiDimension)