"""
This script sets the LUT-color associated to a given microscope channel (indicated by an integer between 1 and 6).
This is similar than via the menu ACQUIFER > Settings > Set channels colors

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
from acquifer.ij.im04.plugins import Hyperstack_Maker
Hyperstack_Maker.setChannelColor(4, "red") # set channel 4 to red-LUT