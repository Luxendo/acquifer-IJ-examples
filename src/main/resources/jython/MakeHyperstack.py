"""
From a directory, a well and subposition, this scripts list the image files and make a hyperstack for a selected well and subposition.
the following variables should be updated to match your local image dataset:
- inputDir
- selectedWell and selectedSubpositions
- listChannel, Zslice and Timepoint

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
from acquifer.core.im04       import FileUtils
from acquifer.ij.im04.plugins import Hyperstack_Maker
"""
# Use following imports for IM03
from acquifer.core.im03       import FileUtils
from acquifer.ij.im03.plugins import Hyperstack_Maker_IM03
"""
from acquifer.ij.Utils        import printArray # print each item of a list to a new line in the log window (more readable)
from ij import IJ

inputDir = r"C:\Users\Laurent Thomas\Documents\Acquifer\DataSet\Fish\Clicking_AppNote96"

# Select a single well and single subposition
selectedWell = ["A002"]
selectedSubpositions = [1] # first subposition
listChannel   = None # if None or [], all available channels will be displayed, same for other dimensions
listZslice    = None
listTimepoint = None

listFiltered = FileUtils().getListImageFiles(inputDir, 
                                             selectedWell, 
                                             selectedSubpositions, 
                                             listChannel, 
                                             listZslice, 
                                             listTimepoint)
IJ.log("\nList files")
printArray(listFiltered)

# Get metadatas
listMetadatas = FileUtils().getListMetadatas(listFiltered)
IJ.log("\nImages metadata")
printArray(listMetadatas)

# Make hyperstacks
hyperstack = Hyperstack_Maker().makeHyperStack(listMetadatas)
hyperstack.show()