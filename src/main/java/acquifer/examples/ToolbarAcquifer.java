package acquifer.examples;

import acquifer.core.TcpIp;
import ij.IJ;
import ij.gui.Toolbar;
import ij.plugin.PlugIn;

/** This PlugIn will just add custom PlugInTools for TcpIp control to the ImageJ toolbar when clicked. */
public class ToolbarAcquifer implements PlugIn {
	
	public ToolbarAcquifer(){
	}
	
	/** This method is called when this plugin is clicked in the ImageJ menu. */
	@Override
	public void run(String arg) {
		
		TcpIp im;
		
		try { 
			im = new TcpIp(); // open the communication port with the IM
		}
		
		catch (Exception error) {
			IJ.error(error.getMessage());
			error.printStackTrace();
			return; // The toolbar is not populated in this case
		}
		
		Toolbar.addPlugInTool(new MoveIMToClick(im));
		Toolbar.addPlugInTool(new SwitchToLive(im));
		
	}

}