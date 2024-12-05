"""
Opening .ome.tif images as single plane.
A bit different than normal tiff as IJ.openImage directly loads all planes, so one has to use the lower level Opener().openTiff
"""

from ij import IJ
from ij.io import Opener

pathA1 = r"C:\Users\Laurent.Thomas\Documents\Dataset\20241128_153149_test-ome\-A001--PO01--LO001--CO1--SL001--PX32500--PW0030--IN0020--TM242--X014535--Y010809--Z175000--T0000000000--WE00001.ome.tif"
pathB2 = r"C:\Users\Laurent.Thomas\Documents\Dataset\20241128_153149_test-ome\-B002--PO01--LO001--CO2--SL001--PX32500--PW0050--IN0050--TM242--X023543--Y019807--Z175000--T0000004959--WE00023.ome.tif"

#image = IJ.openImage(pathB2) # this would open the stack and seems to load A1 instead, not sure
opener = Opener()

# openTiff allows to open a single plane instead
image1 = opener.openTiff(pathA1, 1)
image2 = opener.openTiff(pathB2, 1)

image1.show("A1")
image2.show("A2")