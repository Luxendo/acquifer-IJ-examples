"""
This jython script demonstrates how to create a Metadata object from different sources: a java File object, a full or partial file path or a simple filename.
Similarly than with a MetadataParser, one can recover values of specific metadata from a Metadata object.
In particular, one can write code using Metadata Object that will work for both IM03 and IM04, since the accessible methods are the sames.

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
from acquifer.core.im04 import Metadata
from java.io import File
import os

# There are different ways to create a Metadata object

## From an absolute filepath
imagePath = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\ValerioSubset\-A001--PO01--LO003--CO5--SL009--PX16250--PW0100--IN0100--TM286--X015530--Y010642--Z204727--T0028985883--WE00001.tif"
m1 = Metadata(imagePath)
print m1, "exists:", m1.exists()

## From a java File object
imageFile = File(imagePath)
m2 = Metadata(imageFile)
print m2, "exists:", m2.exists()

## From an image name
imageName = "-A001--PO01--LO003--CO6--SL001--PX16250--PW0100--IN0030--TM285--X015530--Y010642--Z206327--T0028987029--WE00001.tif"
m3 = Metadata(imageName)
print m3, "exists:", m3.exists()

## From a partial filepath
incompletePath = os.path.join("myDir", imageName) 
m4 = Metadata(incompletePath)
print m4, "exists:", m4.exists()



# One can recover any metadata contained in the filename, as with the MetadataParser
# See the API documentation for a list of available functions
# https://acquifer.github.io/acquifer-core/acquifer/core/im/Metadata.html
print "Pixels size (micrometers):", m1.getPixelSize()
print "Z-Position (micrometers): ", m1.getPositionZ()