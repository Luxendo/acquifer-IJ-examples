"""
This scripts demonstrates how to activate temperature regulation externally.
The target temperature for the sample can range between 18 to 34 degrees Celsius. 
2 solutions are shown to start a script once the temperature has stabilize
Option 1 : waiting for a fixed time interval before starting the script
Option 2 : Actively checking the temperature regularly to know if it has reached the target value
"""
from acquifer.core import TcpIp
from java.util.concurrent import TimeUnit

myIM = TcpIp() # open the communication port with the IM

# Define the target temperature for incubation, switch on regulation
# and wait for a few minutes that temperature is stable (half an hour would be a better value)
targetTemp = 25.2
margin = 0.5 # accept deviation from the target temperature 
myIM.setTemperatureTarget(targetTemp)  # in degrees Celsius with 1 decimal precision max
myIM.setTemperatureRegulation(True)    # turn on the regulation


# OPTION 1 : wait for a given number of minutes, to let time for the temperature to stabilize
minutesToWait = 30 
print "Waiting {} minutes for temperature to stabilize.".format(minutesToWait)
TimeUnit.MINUTES.sleep(minutesToWait)


# OPTION 2 : Check every 5 minutes what is the current sample temperature
# Starts only if at least twice successive times (separated by the selected waitInterval) in the expected range
inRange1 = False
inRange2 = False
waitInterval = 5
while not (inRange1 and inRange2):
	
	# Wait another interval
	TimeUnit.MINUTES.sleep(waitInterval)
	
	# Check the temperature after waiting
	print "-> Checking temperature..."
	currentTemp = myIM.getTemperatureSample()
	
	# Check if in range target +/- margin
	if (targetTemp - margin <= currentTemp and currentTemp <= targetTemp + margin): # in-range
	
		if (inRange1): # last timepoint already in-range
			inRange2 = True
			print "Temperature is in range (again), about to start experiment..."
	
		else:
			inRange1 = True
			print "Temperature is in range (1st-time)"
	
	
	else: # Not in range -> Reset "history"
		print "Temperature not in range, still waiting for {} minutes".format(waitInterval)
		inRange1 = False
		inRange2 = False

# Here we use a raw-string (prefixed with r), to prevent backslash to be interpreted as special character such as new line for \n
# You dont need raw string if your path is using forward slash / or double back slash \\ as separator
print "Starting the experiment"
experimentPath = r"C:\Users\Admin\Example\myScript.imsf"
myIM.runScript(experimentPath) # This will pause further code execution until the script is finished running

myIM.closeConnection()
print "Done"
