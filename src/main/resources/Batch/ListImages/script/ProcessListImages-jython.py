"""
This script can be saved to disk and used as a custom jython script (.py extension) with the plugin "Batch process images (script)"
It demonstrates how to execute a custom script for each image file in an IM experiment directory, that satisfies the dimensions selected in the GUI.
The code below would be very similar for another scripting language.

Scripts to use with the "Batch process images (script)" should have a single script-parameters of type File and named "image_path" as below.
The custom script will be called for every image file matching the dimension slected in the plugin's GUI.
The image file is passed directly as a File object (https://docs.oracle.com/javase/7/docs/api/java/io/File.html). 
From this File object, you can recover the filepath as shown below.
From there you can open the image in Fiji or process the file without opening the image (e.g. to move files around).

Use File > Save As... to save a copy of this example, and keep your modifications.
You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
"""
#@ File image_file
from ij import IJ, ImagePlus
import time

IJ.log("\nFilepath : " +  image_file.getPath())
IJ.log("Filename :   " +  image_file.getName())
IJ.log("Directory :  " +  image_file.getParent())

# Create an ImagePlus from the filepath
filepath = image_file.getPath()
imp = ImagePlus(filepath)

# You can display the image, although everything can be done headless with the ImagePlus object
imp.show()
IJ.log("\nWaiting 3 secs before closing image")
time.sleep(3)
imp.close()



