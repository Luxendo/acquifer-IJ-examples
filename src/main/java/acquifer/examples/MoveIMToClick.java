package acquifer.examples;

import java.awt.Font;
import java.awt.Point;
import java.awt.event.MouseEvent;

import acquifer.core.TcpIp;
import acquifer.core.im04.MetadataParser;
import fiji.util.gui.GenericDialogPlus;
import ij.IJ;
import ij.ImagePlus;
import ij.gui.ImageCanvas;
import ij.plugin.tool.PlugInTool;

/** This plugin is an ImageJ menu click tool, to direct the Imaging Machine to the clicked position in a previously acquired image and/or perform AF + acquisition. <br>
 * When executed via the menu (it is listed as another plugin in the ACQUIFER menu, see plugins.config), a new icon appears in the ImageJ toolbar. <br>
 * This plugin requires to have the IM connected to the pc and the IM software running. */
public class MoveIMToClick extends PlugInTool {
	
	private TcpIp im;
	private MetadataParser parser;
	
	/** 1-based index of the objective in the IM-system */
	private int objectiveIndex = 1;
	private int selectedChannel = 0; // 0-based -> retrieve label and code via the LIST_CHANNELS  
	private int detectionFilter = 1; 
	
	private boolean doAF;
	private int powerAF = 50;
	private int exposureAF = 50;
	private int nSlicesAF = 10;
	
	/** Distance between slices in µm with 0.1 precision. */
	private double dZ_AF = 10;
	
	private boolean doAcquisition;
	private int power = 50;
	private int exposure = 50;
	private int nSlices = 10;
	
	/** Distance between slices in µm with 0.1 precision. */
	private double dZ = 10;
	private String outputDir; 
	
	/** Go back to live mode after acquisition. This should be deactivated for successive clicks. */
	private boolean backToLive;

	private final String[] LIST_OBJECTIVES = new String[] {"2x", "4x", "10x", "20x"};
	private final String[] LIST_CHANNELS_ID = new String[] {"BF", "Fluo1", "Fluo2", "Fluo3", "Fluo4", "Fluo5", "Fluo6"};
	private final String[] LIST_CHANNELS_CODE = new String[] {"BF", "100000", "010000", "001000", "000100", "000010", "000001"};
	
	public MoveIMToClick(){
		;
	}
	
	@Override
	public void run(String arg) {
		super.run(arg);
		try { 
			im = new TcpIp(); // open the communication port with the IM
		}
		
		catch (Exception error) {
			IJ.error(error.getMessage());
			//throw new Exception(error); // still throw an error to interrupt code execution
		}
		parser = MetadataParser.getInstance();
	}
	
	@Override
	public String getToolIcon() {
		return "T1d15IT4d15M"; // IM font size 15, x = 1, y = 13 i.e d in hex, see https://imagej.nih.gov/ij/developer/macro/macros.html#icons
	}
	
	@Override
	public void showOptionsDialog() {
		
		GenericDialogPlus dialog = new GenericDialogPlus("IM Click control");
		dialog.addChoice("Objective", LIST_OBJECTIVES, LIST_OBJECTIVES[objectiveIndex-1]); // -1 since ObjectiveIndex is 1-based
		dialog.addChoice("Channel", LIST_CHANNELS_ID, LIST_CHANNELS_ID[selectedChannel]);
		dialog.addNumericField("Detection filter", detectionFilter);
		
		dialog.addMessage("Autofocus settings", dialog.getFont().deriveFont(Font.BOLD));
		dialog.addCheckbox("Run software autofocus", doAF);
		dialog.addNumericField("Illumination intensity (%)", powerAF);
		dialog.addNumericField("Exposure time (ms)", exposureAF);
		dialog.addNumericField("Number of Z-slices", nSlicesAF);
		dialog.addNumericField("Z-slice spacing (µm)", dZ_AF);
		
		dialog.addMessage("Acquisition settings", dialog.getFont().deriveFont(Font.BOLD));
		dialog.addCheckbox("Acquire Z-stack", doAcquisition);
		dialog.addNumericField("Illumination intensity (%)", power);
		dialog.addNumericField("Exposure time (ms)", exposure);
		dialog.addNumericField("Number of Z-slices", nSlices);
		dialog.addNumericField("Z-slice spacing (µm)", dZ);
		dialog.addDirectoryField("Save images in...", outputDir);
		
		dialog.addCheckbox("Come_back to live mode (deactivate for succesive clicks)", backToLive);
		
		dialog.showDialog();
		
		
		
		if (dialog.wasOKed()) {
			
			objectiveIndex = dialog.getNextChoiceIndex() + 1;
			selectedChannel = dialog.getNextChoiceIndex();
			detectionFilter = (int) dialog.getNextNumber(); // TODO should check in range
			
			// AF settings
			doAF = dialog.getNextBoolean();
			powerAF = (int) dialog.getNextNumber();
			exposureAF = (int) dialog.getNextNumber();
			nSlicesAF = (int) dialog.getNextNumber();
			dZ_AF = dialog.getNextNumber();
			
			// Acquisition settings
			doAcquisition = dialog.getNextBoolean();
			power = (int) dialog.getNextNumber();
			exposure = (int) dialog.getNextNumber();
			nSlices = (int) dialog.getNextNumber();
			dZ = dialog.getNextNumber();
			outputDir = dialog.getNextString();	
			backToLive = dialog.getNextBoolean();
		}
	}
	
	@Override
	public void mouseClicked(ImagePlus imp, MouseEvent e) {
		
		super.mouseClicked(imp, e);
		
		// Get image canvas and add click listener
		ImageCanvas canvas = imp.getCanvas();
		/*
		 int x = canvas.offScreenX(e.getX());
		 int y = canvas.offScreenY(e.getY());
		*/
		
		// Get metadata used for the coordinates calculations
		String imageName = imp.getTitle();

		// Get clicked coordinates
		Point point = canvas.getCursorLoc(); // directly in pixels within the image, independent of the zoom
		
		double[] xy_mm = TcpIp.convertXYpixelToMillimeters(point.x, 
														   point.y,
														   imageName, 
														   imp.getWidth(),
														   imp.getHeight());

		System.out.println(String.format("x,y (pixels) : %s,%s", point.x, point.y)); // printed to the ImageJ console window. Not automatically opened
		System.out.println(String.format("x,y (mm)     : %s,%s", xy_mm[0], xy_mm[1])); // printed to the ImageJ console window. Not automatically opened
		
		
		// Extract Z and well ID from imageName
		double z_um = parser.getPositionZ(imageName) * 1000; //  before acquifer-core 3.3.0, return in mm
		// double z_um = parser.getPositionZ(imageName); // TODO update for acquifer-core 3.3.0 getPositionZ is in µm 
		
		// Move to XY
		im.moveXYto(xy_mm[0], xy_mm[1]);
		im.setMode("script"); // script mode before AF and acquisition
		
		
		String lightSource = LIST_CHANNELS_CODE[selectedChannel];
		
		if (doAF) {
			
			// Overwrite z_um with zFocus
			// Run AF using Z of the image as center
			z_um = im.runSoftwareAutoFocus(objectiveIndex,	
										   lightSource, 
										   detectionFilter, 
										   powerAF, 
										   exposureAF, 
										   z_um,
										   nSlicesAF, 
										   dZ_AF);
												  
			// print "Z-focus :", z_um
		}
		
		if (doAcquisition) {
			// Acquire
			im.setMetadataWellId(parser.getWellId(imageName));
			im.acquire(1,
					   objectiveIndex, 
					   lightSource, 
					   detectionFilter, 
					   power, 
					   exposure, 
					   z_um,
					   nSlices, 
					   dZ,
					   false, // lightConstant
					   outputDir);
		}
		
		if (backToLive) {
			// Back to live mode after acquisition
			// Switch on light source 
			im.setMode("live");
			im.setLightSource(1, lightSource, detectionFilter, power, exposure);
			im.moveZto(z_um); // move to focused position
		}
	}
}