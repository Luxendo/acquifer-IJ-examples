"""
This scripts demonstrates how to switch-on/off light sources.

There 2 types of light sources in the IM :
- the brightfield light source located in the lid (transmitted light).

- the LED light sources used for fluorescence excitation
There are 6 built-in LED light sources each with a specific excitation spectra. 
You can switch-on one at a time or multiple LED light sources at once.
The way the LED light-sources are encoded in this API is a 6-character long string (1 per LED) with value 0/1 respectively if the LED should be off/on.

Example :
100000 : switch-on first LED
010000 : switch on second LED
100001 : switch on both first and last LED

When switching multiple LED at once, the user-defined illumination intensity is applied to each selected LED.
Example 50% with LED 1 and 2 will result in both LED set to 50%.

# Note about the live/script mode
In live mode (default if no script is running), the light source is directly activated upon sending the command.
A "switch-off" command should thus be sent to switch-off the light source.

In script mode, the light source are switched on/off automatically while the camera is acquiring images.
There is thus no need to send a switch-off command in this case.

# lightConstantOn option
By default this option is set to false, meaning that the light is not constantly on but is rather synchronized with the camera exposure time.  
This results in having the light-source blinking, hence reducing phototoxicity compared to having the light constantly on during the acquisition phases.
However, if you want to avoid your sample being exposed to a flashing light, you can set this option lightConstantOn to true, and thus have a constant illumination during acquisition phase.
"""
from acquifer.core import TcpIp
from java.lang import Thread

myIM = TcpIp() # open the communication port with the IM


# Set Brightfield on/off
channelNumber = 1   # this is for filenaming only, the CO* tag
detectionFilter = 2 # positional index of the detection filter (1 to 4), depending on the filter, the overall image intensity varies.
intensity = 50 # relative intensity
exposure = 100 # camera exposure in ms for this channel
lightConstantOn = False

myIM.setBrightField(channelNumber, detectionFilter, intensity, exposure) # default lightConstantON = false
myIM.setBrightField(channelNumber, detectionFilter, intensity, exposure, lightConstantOn) # alternative call with custom lightConstant

Thread.sleep(5000) # wait 5 seconds, ie leave the light on for 5 sec 

myIM.setBrightFieldOff() # switch off the brightfield, this also stops the camera preview



# Fluo
channelNumber = 2
lightSource = "010000"
detectionFilter = 3
intensity = 50
exposure = 80

myIM.setFluoChannel(channelNumber, lightSource, detectionFilter, intensity, exposure) # here also default to lightConstantOn False
myIM.setFluoChannel(channelNumber, lightSource, detectionFilter, intensity, exposure, lightConstantOn) # here custom value for lightConstantOn

Thread.sleep(5000) # wait 5 seconds

myIM.setFluoChannelOff() # switch off the fluo channel, this also stops the camera preview


"""
You can also use setLightSource/setLightSourceOff which works for both brightfield and fluorescence.
The light source is specified as a string and should be either the 6-digit string of 0/1 as in setFluoChannel
or one of "brightfield" or "bf" (not case-sensitive)
"""
# Switch on again the fluo light-source (we just reuse the variables from above)
myIM.setLightSource(channelNumber, lightSource, detectionFilter, intensity, exposure)
Thread.sleep(5000)
myIM.setLightSourceOff(lightSource)

# This one is to switch the brightfield on 
lightSource = "bf" # it could also be "brightfield"
myIM.setLightSource(channelNumber, lightSource, detectionFilter, intensity, exposure)
Thread.sleep(5000)
myIM.setLightSourceOff(lightSource)

# Closing the connection also switch off any light source if there are any still on
myIM.closeConnection()