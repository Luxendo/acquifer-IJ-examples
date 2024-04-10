package acquifer.toolbarIM;

import java.awt.Font;
import java.awt.Point;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.nio.file.Paths;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import ij.Prefs;

import acquifer.core.TcpIp;
import acquifer.core.im04.MetadataParser;
import fiji.util.gui.GenericDialogPlus;
import ij.IJ;
import ij.ImageJ;
import ij.ImagePlus;
import ij.ImageStack;
import ij.gui.ImageCanvas;
import ij.plugin.tool.PlugInTool;

/** This plugin is an ImageJ menu click tool, to direct the Imaging Machine to the clicked position in a previously acquired image and/or perform AF + acquisition. <br>
 * When executed via the menu (it is listed as another plugin in the ACQUIFER menu, see plugins.config), a new icon appears in the ImageJ toolbar, and get automatically activated. <br>
 * Upon activation of the tool, a TcpIp connection to the IM is established.<br>
 * With the tool selected, and an IM image opened in Fiji, clicking on the image will move the objective XY-position to the clicked position.<br>
 * If selected in the tool configuration window (double-click on the tool icon), the click can also perform software autofocus and/or acquisition of a Z-stack.<br>
 * The z-start for the autofocus is the image Z-position, same for the acquisition, except if autofocus is performed then the focus position is used for the z-center of the stack.<br>
 * This plugin requires to have the IM connected to the pc and the IM software running. <br> 
 * */
public class MoveIMToClick extends PlugInTool implements KeyListener {
	
	private TcpIp im;
	private MetadataParser parser;
	
	/** 1-based index of the objective in the IM-system */
	private int objectiveIndex = 1;
	private int selectedLightsourceIndex = 0; // 0-based -> retrieve label and code via the LIST_CHANNELS  
	private int detectionFilterIndex = 0; 
	
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
	private String outputDir = Prefs.get("click.outputDir", 
										  Paths.get(IJ.getDirectory("home"), "ACQUIFER_ClickTool").toString()); 
	
	/** Go back to live mode after acquisition. This should be deactivated for successive clicks. */
	private boolean backToLive = true;

	private final String[] LIST_OBJECTIVES = new String[] {"2x", "4x", "10x", "20x"};
	
	/** The list of channel shown in the dialog, this list is only used to get the index of the selected channel, and the index is then used to get the actual light source from LIST_LIGHTSOURCES */ 
	private final String[] LIST_LIGHTSOURCES_ID = new String[] {"BF", "Fluo1", "Fluo2", "Fluo3", "Fluo4", "Fluo5", "Fluo6"};
	
	/** String encoded light source, either "BF" or a string of six 0/1 for the LED sources. <br> 
	 * Given the index of the channel selected in LIST_CHANNELS_ID, get the corresponding LIGHTSOURCE. <br> 
	 * This could have been replaced by a mapping CHANNEL : LIGHT_SOURCE*/
	private final String[] LIST_LIGHTSOURCES = new String[] {"BF", "100000", "010000", "001000", "000100", "000010", "000001"};
	
	private final String[] LIST_FILTERS = new String[]{"1","2","3","4","5"};
	
	/** Constructor called by the ToolbarAcquifer passing the newly created connection to the IM. */
	public MoveIMToClick(TcpIp im){
		this.im = im;
		parser = MetadataParser.getInstance();
		
		// Try adding this plugin as a listener to the ImageJ window
		ImageJ imageJ = IJ.getInstance();
		imageJ.addKeyListener(this);
	}
	
	/** This is called when the plugin is run from the menu but it does not seem to be called when the tool is selected in the toolbar. */
	@Override
	public void run(String arg) {
		super.run(arg);
	}
	
	/** Shown when the mouse is hovered over the toolbar icon. */
	@Override
	public String getToolName() {
		return "Move objective to clicked coordinates and AF/Acquire. Double-click to configure.";
	}
	
	@Override
	public String getToolIcon() {
		// generated with the image to hex macro from Mutterer J. https://imagej.net/ij/macros/tools/Image_To_Tool_Icon.txt
		return "C000C111C222C333C444C555C666D44D45D46D47D48D55D56D57D65D66D67D76C666D58C666D54C666D49D86C666D75C666D77C666D43C666C777D68C777D64C777C888D33C888D34C888D59C999D35C999D36C999D85C999D37C999D96C999D38C999D39C999D87C999D53CaaaD32CaaaD4aCaaaD3aCaaaCbbbD78CbbbD74CbbbCcccD42CcccCdddD69CdddD95CdddCeeeD63CeeeD97CeeeD5aCeeeD3bCeeeCfffDa6CfffD84CfffD22D23CfffD24D25D31D88CfffD52CfffD26CfffD27CfffD28D4bCfffD29CfffD2aCfffDa5CfffD73D79CfffD21D2bD41CfffD6aD94Da7CfffD00D01D02D03D04D05D06D07D08D09D0aD0bD0cD10D11D12D13D14D15D16D17D18D19D1aD1bD1cD20D2cD30D3cD40D4cD50D51D5bD5cD60D61D62D6bD6cD70D71D72D7aD7bD7cD80D81D82D83D89D8aD8bD8cD90D91D92D93D98D99D9aD9bD9cDa0Da1Da2Da3Da4Da8Da9DaaDabDacDb0Db1Db2Db3Db4Db5Db6Db7Db8Db9DbaDbbDbcDc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9DcaDcbDcc";
		//return "icon:icon.png";
	}
	
	@Override
	public void showOptionsDialog() {
		
		GenericDialogPlus dialog = new GenericDialogPlus("IM Click control");
		dialog.addChoice("Objective", LIST_OBJECTIVES, LIST_OBJECTIVES[objectiveIndex-1]); // -1 since ObjectiveIndex is 1-based
		dialog.addChoice("Light source", LIST_LIGHTSOURCES_ID, LIST_LIGHTSOURCES_ID[selectedLightsourceIndex]);
		dialog.addChoice("Detection filter", LIST_FILTERS, LIST_FILTERS[detectionFilterIndex]);
		
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
			selectedLightsourceIndex = dialog.getNextChoiceIndex();
			detectionFilterIndex = dialog.getNextChoiceIndex();
			
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
			
			Prefs.set("click.outputDir", outputDir);
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
		String imageName;
		if (imp.isHyperStack()) { // make it compatible with the OpenInFiji tool
			
			int sliceIndex = imp.getCurrentSlice(); // 1-based, reflect also hyperstack sliders
			
			ImageStack stack = imp.getImageStack();
			imageName = stack.getSliceLabel(sliceIndex);
		}
		
		else {
			imageName = imp.getTitle();
		}

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
		//double z_um = parser.getPositionZ(imageName) * 1000; //  before acquifer-core 3.3.0, return in mm
		double z_um = parser.getPositionZ(imageName); // acquifer-core >= 3.3.0 getPositionZ is in µm 
		
		// Set selected objective 
		// if no AF nor acquisition need to be done manually
		if (!doAF && !doAcquisition) {
			im.setObjective(objectiveIndex);
		}
		
		// Move to XY
		IJ.log("\nMoving objective to clicked XY position, and Z-position of original image");
		//im.moveXYto(xy_mm[0], xy_mm[1]);		
		im.moveXYZto(xy_mm[0], xy_mm[1], z_um); // also move Z, TODO check if needed
		
		// from the channel selected by the user, get the corresponding light source
		String lightSource = LIST_LIGHTSOURCES[selectedLightsourceIndex]; 
		
		if (doAcquisition) {
			im.setMode("script"); // script mode before AF and acquisition
			// since the same objective is used for AF and autofocus
			// when coming from live mode avoid "objective reset" that would otherwise happen after AF, when switching to script mode before acquisition

		}
		
		if (doAF) {
			
			IJ.log("Running Autofocus");
			// Overwrite z_um with zFocus
			// Run AF using Z of the image as center
			z_um = im.runSoftwareAutoFocus(objectiveIndex,	
										   lightSource, 
										   detectionFilterIndex + 1, // filter index is 0-based 
										   powerAF, 
										   exposureAF, 
										   z_um,
										   nSlicesAF, 
										   dZ_AF);
												  
			// print "Z-focus :", z_um
			
			// if not acquiring show the focused position
			if (!doAcquisition) 
				previewAtPosition(z_um, lightSource);
			}
		
		
		if (doAcquisition) {
			
			// Make a unique subdirectory with a timestamp
			DateFormat df = new SimpleDateFormat("yyyyMMdd_hhmmss"); // add S if you need milliseconds
			String saveDir = Paths.get(outputDir, df.format(new Date())).toString();
			IJ.log("Acquire and save images in:");
			IJ.log(saveDir);
			
			// Acquire
			im.setMetadataWellId(parser.getWellId(imageName));
			im.acquireZstack(1,
							 objectiveIndex, 
							 lightSource, 
							 detectionFilterIndex + 1, // filter index is 0-based 
							 power, 
							 exposure, 
							 z_um,
							 nSlices, 
							 dZ,
							 false, // lightConstant
							 saveDir);
			
			if (backToLive) // only needed for acquisition which requires the script mode
				previewAtPosition(z_um, lightSource);
		}
	}
	
	/** Switch back to live mode if not already the case, activate light source and move to Z. */
	public void previewAtPosition(double z_um, String lightSource) {
		im.setMode("live");
		im.setLightSource(1, lightSource, detectionFilterIndex+1, power, exposure);
		im.moveZto(z_um); // move to focused position
	}

	@Override
	public void keyTyped(KeyEvent e) {
		
	}
	
	/** Does not work, this make the plugin a KeyListener but the listener would need to be linked to a canvas or a component accepting a KeyListener.*/
	@Override
	public void keyPressed(KeyEvent e) {
		IJ.log("Pressed");
		
		if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
			//im.setMode("live");
			//System.out.println("Print escape");
			IJ.log("Pressed escape");
			//e.consume(); // needed ?
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
}
