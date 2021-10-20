"""
This jython script demonstrates the parsing of metadata from image filename for images acquired with an Imaging Machine.
This script can be directly run in the Fiji script editor.
It relies on the acquifer-core java package, shipped with the acquifer update site.
These functions can also be used in other java programs, as long as the acquifer-core package is available.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
from acquifer.core.im04 import MetadataParser
#from acquifer.core.im03 import MetadataParser # Uncomment this line for IM03

parser = MetadataParser.getInstance() # recover the unique instance of MetadataParser (singleton design)

# Set an example filename
filename = "-A002--PO01--LO001--CO6--SL001--PX32500--PW0080--IN0020--TM281--X023590--Y011262--Z211710--T0200262822--WE00002.tif"
# Uncomment the following line for IM03
#filename = "WE00019---B006--PO01--LO001--CO6--SL010--PX16250--PW0040--IN0020--TM246--X059308--Y019906--Z212725--T1375564662.tif" # example filename

print "Image name :", filename

print "Well Id :", parser.getWellId(filename) 

print "Plate column :", parser.getWellColumn(filename)
print "Plate row :",    parser.getWellRow(filename)

print "Well subposition :", parser.getWellSubPosition(filename)

print "Well index (order of acquisition) :", parser.getWellIndex(filename)

print "Positions XY (mm): ", parser.getXYPosition(filename).tolist()
print "Position Z (mm): ",   parser.getZPosition(filename)

print "Z-slice Number : ", parser.getZSlice(filename)

print "Light power (%) :", parser.getLightPower(filename)

print "Exposure time (ms) :", parser.getLightExposure(filename)

print "Channel index :", parser.getChannelIndex(filename) 

print "Objective Magnification :", parser.getObjectiveMagnification(filename)

print "Objective NA :", parser.getObjectiveNA(filename)

print "Pixel Size (um): ", parser.getPixelSize(filename)

print "Timepoint :", parser.getTimepoint(filename)

print u"Temperature (°C)", parser.getTemperature(filename) # use unicode "u" string for special ° character