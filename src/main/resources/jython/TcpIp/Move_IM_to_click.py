#@ImagePlus active_imp
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

		except Exception, error :
			IJ.error(error.getMessage())
			raise Exception(error) # still throw an error to interrupt code execution

		
		# Get image canvas and add click listener
		self.canvas = imp.getCanvas()
		self.canvas.addMouseListener(self) # the trick, add the current instance of mouse listener to the canvas
		
		# Get metadata used for the coordinates calculations
		self.imageName = imp.getTitle()
		self.width  = imp.getWidth()
		self.height = imp.getHeight()
	
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
		# Move to XY..
		self.im.moveXYto(x_mm, y_mm)
		
		# Or XYZ with the Z corresponding to the image
		#self.im.moveXYZto(x_mm, y_mm, parser.getPositionZ(imageName))
	
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
