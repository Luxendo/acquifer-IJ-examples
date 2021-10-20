"""
This snippet demonstrates the handling of ImagePlane, which represents a single IM image. 
Typically you obtain ImagePlane via a Dataset object (see the dedicated Dataset example script). 
"""
#@File (label="Image from IM04 dataset", style="file") image_file 
from acquifer.core.im04 import ImagePlane 
from ij import IJ 
 
plane = ImagePlane(image_file.getPath()) 
print "Image Plane :", plane 
 
# Just like wit the MetadataParser, one can recover metadata from an ImagePlane 
print "\nDimensions indexes : "
print "- Channel :",    plane.getChannel() 
print "- Z-slice :",    plane.getZslice() 
print "- Timepoint: ",  plane.getTimepoint() 
print "- Pixel-size: ", plane.getPixelSize() , "um" 
print "- Directory: ",  plane.getDirectoryName() 
 
# Other possible commands 
# Note some attributes (temperature, timepoint...) are read-only attributes 
print "\nList of commands:"
for command in dir(plane):
	print command
 
# Show the image contained in the ImagePlane 
imp = IJ.openImage(plane.getPath()) 
print "\nImagePlus : ", imp 
imp.show()