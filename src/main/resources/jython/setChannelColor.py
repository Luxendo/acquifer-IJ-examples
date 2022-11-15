"""
This script sets the LUT-color associated to a given microscope channel (indicated by an integer between 1 and 6).
This is similar than via the menu ACQUIFER > Settings > Set channels colors

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
from acquifer.ij.im04.plugins import Hyperstack_Maker
Hyperstack_Maker.setChannelLut(4, "Red") # set channel 4 to red-LUT