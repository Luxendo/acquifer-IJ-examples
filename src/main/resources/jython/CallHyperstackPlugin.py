"""
Although not super useful, you can call the hyperstack plugin to show up via scripting too.
Either using macro-recording which will give you something like IJ.run(..)
Or using the command below.

NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
"""
from acquifer.ij.im04.plugins import Hyperstack_Maker
#from acquifer.ij.im03.plugins import Hyperstack_Maker # Uncoment this line for IM03

# Call the plugin
Hyperstack_Maker().run()