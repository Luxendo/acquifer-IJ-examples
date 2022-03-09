"""
This script demonstrates how to actively control the Imaging Machine via an external application
For instance to set a specific objective, and move it across the plate to a given X,Y,Z position.

See the API documentation for the list of commands available by TcpIp and their docstrings. 
https://acquifer.github.io/acquifer-core/acquifer/core/TcpIp.html
"""
from acquifer.core import TcpIp
from java.lang import Thread

myIM = TcpIp() # open the communication port with the IM

# Set a specific objective
myIM.setObjective(2) # this sets the objective mounted at position 2 in the IM, usually the 4X

# Moving the objective along X,Y,Z
# There are 2 options : 
# - "move to" Absolute movement to given X,Y and/or Z coordinates
# - "move by" Relative movement to move by a given step-size along the X,Y and/or Z axis

x = 10.123 # mm with max 3 decimal places
y = 30.456

# Move XY
print "Moving XY"
myIM.moveXYto(x,y)
print "Waiting 5 seconds before next move"
Thread.sleep(5000) # wait 5 seconds before moving (so you can see it)
myIM.moveXYby(10.2, -5.5) # Move by another 10.2 mm along x, move back by 5.5 mm along y

# Move Z
z = 456.1 # micrometers with max 1 decimal place
print "Moving Z"
myIM.moveZto(z)
print "Waiting 5 seconds before next move"
Thread.sleep(5000) # wait 5 seconds before moving (so you can see it)
myIM.moveZby(3.3)

# Move X,Y,Z all at once
# For this one there is only the absolute movement version
Thread.sleep(5000) # wait 5 seconds before moving (so you can see it)
print "Moving XYZ"
myIM.moveXYZto(x,y,z)

#myIM.closeConnection() # This would switch off light-sources and stop the camera preview. Commented by default but feel free to uncomment
print "Done"