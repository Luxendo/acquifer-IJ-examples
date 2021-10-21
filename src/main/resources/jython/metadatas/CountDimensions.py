"""
This jython script demonstrates how to inspect the content of a dataset to find the uniques values available for each dimensions.
More precisely, it shows how to find unique wells, subpositions, channels, z-slices and timepoints available.
and/or how many unique values are available for each dimensions

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
listFull = utils.getListMetadatas(image_directory) # without additional parameters, all IM image files are returned

print "Sizes"
print Metadata.dimensionsSizes([])
print Metadata.dimensionsSizes(listFull[0:1])
print Metadata.dimensionsSizes(listFull)

print "\nContent"
print Metadata.dimensionsContent([])
print Metadata.dimensionsContent(listFull[0:1])
content = Metadata.dimensionsContent(listFull)
print content

# Note content is a dictionary (in python) or mapping (in other languages)
# with Metadata.Dimensions as keys which includes WELL, SUBPOSITION, TIME, Z, CHANNEL
print "\nkey type :", type(content.keys()[0])

zContent = content.get(Metadata.Dimensions.Z)
print "content Z : ", zContent

# You could also first store Dimensions in a variable
dimensions = Metadata.Dimensions
print "content well : ", content.get(dimensions.WELL)

# The content of a dimension is a Set, which is like a list with no duplicate elements
# See https://docs.oracle.com/javase/7/docs/api/java/util/HashSet.html
# You can check if a dimension contains a specific values with contains(value)
print "Z contains slice 5 : ", zContent.contains(5) 

# Finally you can convert the set to a list
listZ = list(zContent)
print "z content as a list ", listZ