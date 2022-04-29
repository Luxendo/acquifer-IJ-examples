"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

This scripts demonstrates a number of values which can be recovered from the Imaging Machine such as temperature, current axis position...

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
from acquifer.core import TcpIp

try : 
	myIM = TcpIp() # open the communication port with the IM

except Error, error :
	IJ.error(error.getMessage())
	raise Exception(error) # still throw an error to interrupt code execution

# Check temperature sensor values
# There are 2 sensors, one for the ambient temp, and one for the sample temp
# Note : the prefix u before the string defines a unicode string to make sure the special character ° is displayed correctly 
print "\nAmbient temperature (Celsius) : ", myIM.getTemperatureAmbient();
print "Sample temperature (Celsius) : ",    myIM.getTemperatureSample();
print "Target Temperature (Celsius) : ",    myIM.getTemperatureTarget(); # that`s the user-defined temperature, either define in the GUI or with setTemperatureTarget 
print "Temperature regulation is on : ", myIM.isTemperatureRegulated();

# Check the current objective
# This is the positional index of the objective in the rack, between 1 and 4, normally with increasing magnifications
# Use setObjective(index) to position another objective
print "\nObjective index : ", myIM.getObjectiveIndex(); 

# X,Y,Z-Position of the objective 
print "\nX-position (mm) : ", myIM.getPositionX(); # mm
print "Y-position (mm) : ",   myIM.getPositionY(); # mm
print "Z-position (micrometers) : ",  myIM.getPositionZ(); # micrometers !! different than X,Y !!

# Mode, either script/live
# In live mode, any change is reflected directly in the IM software ex : switching on/off light sources
# Script mode should be used for repetitive calls to the command acquire, which requires the script mode.
# Activating script mode beforehand in this case, prevents switching back and forth between live/script mode.
# In script mode, interaction with the graphical user interface of the IM software are not possible
# Use myIM.setMode("live") / myIM.setMode("script") to change the current mode
print "\nMode : ", myIM.getModeAsString();
print "Live mode active : ",  myIM.isLiveMode();
print "Script mode active :", myIM.isScriptMode();

# Lid status (open/close)
# Use myIM.openLid() / myIM.closeLid() to move the Lid accordingly
print "\nLid is closed", myIM.isLidClosed();
print "Lid is opened", myIM.isLidOpened();

myIM.closeConnection()