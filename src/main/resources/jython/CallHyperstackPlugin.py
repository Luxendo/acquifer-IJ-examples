"""
Although not super useful, you can call the hyperstack plugin to show up via scripting too.
Either using macro-recording which will give you something like IJ.run(..)
Or using the command below.

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
from acquifer.ij.im04.plugins import Hyperstack_Maker
#from acquifer.ij.im03.plugins import Hyperstack_Maker # Uncoment this line for IM03

# Call the plugin
Hyperstack_Maker().run()