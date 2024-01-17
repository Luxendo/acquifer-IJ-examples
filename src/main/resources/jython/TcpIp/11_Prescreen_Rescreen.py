#@ File (label="Template file")  template
#@ File (label="Overview experiment") exp_overview
#@ File (label="High-mag. experiment") exp_rescreen


from acquifer.core import TcpIp
import os

try : 
	myIM = TcpIp() # open the communication port with the IM

except Exception, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

# Run overview acquisition
imageDir = myIM.runScript(exp_overview.getPath()) # This will pause further code execution until the script is finished running

listImages = [os.path.join(imageDir, filename) for filename in os.listdir(imageDir) if filename.endswith(".tif")]

template = IJ.openImage(template.getPath())

# Run template matching
for filepath in listImages : 

	image = IJ.openImage(filepath)
	
	# Run template matching
	

# Run rescreen acquisition : CANT USE RUNSCRIPT
# or need to accept a custom list of positions
imageDir = myIM.runScript(exp_rescreen.getPath()) # This will pause further code execution until the script is finished running

myIM.closeConnection() # closing the connection will automatically switch back to live mode
print "Done"