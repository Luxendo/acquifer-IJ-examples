"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This script demonstrates how to start an acquisition from an external application, using a pre-existing imaging machine script file (.imsf), as generated by the IM software.
The script will first open the lid, wait for 3 seconds, close the lid and run the script.
This script could be adapted for robotic workflow for instance, where instead of wait, a robotic arm could install a new plate.

The experiment file (.imsf) contains all the information to run the experiment (well coordinates, channels, camera settings, image directory)
therefore no other command is usually needed in this scenario. 

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
#@ String (visibility=MESSAGE, value="Clicking OK will open the IM lid, wait for a user-defined time, close the lid and start a pre-defined script.", required=false) msg
#@ File (style="file") script_path
#@ Integer (label="Wait for (secs)", value=5) delay
from acquifer.core import TcpIp
from java.lang import Thread
from ij import IJ

try : 
	myIM = TcpIp() # open the communication port with the IM

except Exception, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

print "Opening lid"
myIM.openLid() 

print "Waiting", delay, "seconds before closing lid and starting"
Thread.sleep(delay * 1000) # pause execution in milliseconds
# here could be commands for a robotic arm to put a new plate, pipet new reagents...

print "Closing lid"
myIM.closeLid()

# Here we use a raw-string (prefixed with r), to prevent backslash to be interpreted as special character such as new line for \n
# You dont need raw string if your path is using forward slash / or double back slash \\ as separator
print "Starting experiment"
dataset_directory = myIM.runScript(script_path.getPath()) # This will pause further code execution until the script is finished running
print "Finished acquisition, images saved in ", dataset_directory

# Just close the port once the script is finished, also switching off any light source if any
myIM.closeConnection()

# Notify that the script finished
IJ.beep()    # play a sound notification
print "Done" # seen in the script editor

# One could even send a mail notification once the experiment is over
# but more complicated