"""
Generate a VirtualPlate and display it, from an IM directory.
The IM directory is expected to contain a dataset with a SINGLE SUBPOSITION
"""

#@ File (label="Select an IM directory", style="directory") image_directory
from acquifer.core.im04 import FileUtils, DatasetBuilder
from acquifer.ij.Utils  import printArray
from acquifer.ij        import VirtualPlate
from acquifer.ij.im.plugins import Hyperstack_Maker
from acquifer.core      import Plate, PlateSeries
from ij import IJ, ImagePlus

dataset = DatasetBuilder(image_directory).build()
plateSeries = PlateSeries.groupByPlateSeries(dataset)[0] # take the first plate series in the directory. There might be multiple plateSeries if there is more than one subposition

layout = Plate.Wells96
downScaling = 10

# Method 1 - Create a VirtualPlate then call toHyperstack
virtualPlate = VirtualPlate(plateSeries, layout, downScaling)
hyperstack = virtualPlate.toHyperstack() 
hyperstack.show()
Hyperstack_Maker.resetDisplayRange(hyperstack) # reset brightness-contrast so the image do not appear black

# Method 2 : directly create a hyperstack
hyperstack2 = VirtualPlate.createHyperstackFromPlateSeries(plateSeries,
													  	  layout,
													  	  downScaling)
hyperstack2.show()
Hyperstack_Maker.resetDisplayRange(hyperstack2)