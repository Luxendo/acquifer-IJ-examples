#@ ImagePlus active_imp
#@ Boolean (label="Run software autofocus", value=True) run_af
#@ String (visibility=MESSAGE, required=false, value="Clicking OK will add a click-listener to the active image.<br>Clicks on the image will move the current Imaging Machine objective to the XY clicked position, and run a software autofocus if selected.") doc
#@ Boolean (label="Run software autofocus", value=True) run_af
#@ String  (label="Objective", choices={"2X", "4X", "10X", "20X"}) objective
#@ String  (label="Light-source", choices={"BF", "Fluo1", "Fluo2", "Fluo3", "Fluo4", "Fluo5", "Fluo6"}) lightsource
#@ Integer (label="Detection filter", min=1, max=4, step=1) detection_filter
#@ Integer (label="Power (%)", min=0, max=100, value=50) power
#@ Integer (label="Exposure (ms)", min=0, value=50) exposure
#@ Integer (label="Number of Z-slices", min=0, value=10) nslices
#@ Double  (label="Z-step size (µm)", min=0, value=10, style="format:#.#") zstep
"""
REQUIREMENTS
- running the script on a control PC/HIVE connected to the IM
- have the IM software opened in parallel of Fiji
- the option "Block remote connection" of the IM software disabled in the admin panel (contact your system administrator or the acquifer support)

The script should be run after opening in Fiji an image acquired with the IM.
Running the script associates a "Click listener" to the current image window, that will respond to clicks on the image.
For each click, the currently selected objective will be moved to the clicked position, i.e the field of view of the IM will be centered on the clicked position.
Only the XY position of the objective is updated, the Z-position is untouched so for better visualization you should activate a channel in the IM software, and adjust the Z position to be in-focus.

A possible use-case is to open a low magnification image (2/4X) and to use a higher magnification objective for preview in the IM software.
Clicking in the low-mag image will thus give you an idea of the field of view with the higher resolution objective. 
"""
from java.awt.event import MouseListener
from acquifer.core  import TcpIp
from acquifer.core.im04 import MetadataParser
from ij.gui import GenericDialog

dico_lightsources = {"BF":"BF",
					 "Fluo1":"100000",
					 "Fluo2":"010000",
					 "Fluo3":"001000",
					 "Fluo4":"000100",
					 "Fluo5":"000010",
					 "Fluo6":"000001"}
dico_objectives = {"2X":1, 
				  "4X":2,
				  "10X":3,
				  "20X":4}
				
class ClickListener(MouseListener):
	"""
	Custom MouseListener that responds to click on an image.
	Click coordinates are turned to IM axis coordinates and the objective is moved to the clicked position.
	Running this script will associate an instance of this custom listener to the current image canvas.
	
	Note : only the mouseClicked method is implemented, other methods are not used but have to be implemented
	(otherwise mother abstract class complains).
	
	NOTE : this works with image acquired with the full camera sensor area, and any binning factor.
	However, IF THE IMAGE WAS ACQUIRED WITH A PARTIAL SENSOR AREA, NOT CENTERED ON THE ORIGINAL SENSOR AREA, THE SCRIPT WONT WORK AS EXPECTED.
	The reason is that the center of the image is expected to match the objective coordinates in the image filename.
	However, if the sensor area is not centered on the original field of view, the center of the image wont correspond to the objective position.
	"""
	
	def __init__(self, imp):
		
		try : 
			self.im = TcpIp() # open the communication port with the IM

		except Error, error :
			IJ.error(error.getMessage())
			raise Exception(error) # still throw an error to interrupt code execution

		
		# Get image canvas and add click listener
		self.canvas = imp.getCanvas()
		self.canvas.addMouseListener(self) # the trick, add the current instance of mouse listener to the canvas
		
		# Get metadata used for the coordinates calculations
		self.imageName = imp.getTitle()
		self.width  = imp.getWidth()
		self.height = imp.getHeight()
		self.parser = MetadataParser.getInstance()
	
	def mouseClicked(self, mouseEvent):
		"""Print to the console below the x,y coordinates relative to the canvas i.e same than ImageJ coordinates.""" 
		
		point = self.canvas.getCursorLoc() # directly in image coordinates, independent of the zoom
		x, y = point.x, point.y
		print "x,y:", x, y
		
		x_mm, y_mm = TcpIp.convertXYpixelToMillimeters(x, 
													   y,
													   self.imageName, 
													   self.width,
													   self.height)
		print "x,y (mm):", x_mm, y_mm
		z_mm = self.parser.getPositionZ(self.imageName)
				
		# Move to XYZ with the Z corresponding to the image
		self.im.moveXYto(x_mm, y_mm)
		
		if run_af:
			# Run AF using Z of the image as center
			zFocus = self.im.runSoftwareAutoFocus(dico_objectives[objective],	
												  dico_lightsources[lightsource], 
												  detection_filter, 
												  power, 
												  exposure, 
												  z_mm,
												  nslices, 
												  zstep)
			self.im.moveZto(zFocus) # not sure this is needed, the AF might leave the objective axis to the most focused position
		
	
	def mouseEntered(self, mouseEvent):
		pass
	
	def mouseExited(self, mouseEvent):
		pass
	
	def mousePressed(self, mouseEvent):
		pass
	
	def mouseReleased(self, moouseEvent):
		pass


# Create an instance of the ClickListener with the active image
listener = ClickListener(active_imp)
"""
# Create a GUI to collect AF parameters
dialog = GenericDialog("IM click control")
dialog.addCheckbox("Run Autofocus")
dialog.addChoice("Objective", range(1,5), 1)
dialog.addChoice("Light-source", ["BF", "Fluo1", "Fluo2", "Fluo3", "Fluo4", "Fluo5", "Fluo6"], "BF")
dialog.addChoice("Filter", range(1,5), 1)
"""