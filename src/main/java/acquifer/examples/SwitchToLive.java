package acquifer.examples;

import java.awt.event.MouseEvent;

import acquifer.core.TcpIp;
import ij.IJ;
import ij.IJEventListener;
import ij.gui.Toolbar;
import ij.plugin.tool.PlugInTool;

/** This simple plugin establish a connection to the IM and switch back to live mode.*/
public class SwitchToLive extends PlugInTool implements IJEventListener {
	
	private TcpIp im;
	private String name = "Switch IM to live mode";
	
	public SwitchToLive(TcpIp im){
		this.im = im;
		IJ.addEventListener(this); // the plugin will get notified by ImageJ for IJevent
	}
	
	/** This is called if the plugin would be run from a menu. */
	@Override
	public void run(String arg) {
		//IJ.log("run");
	}
	
	/** This name is shown in the ImageJ status bar. */
	@Override
	public String getToolName() {
		return name;
	}
	
	@Override
	public String getToolIcon() {
		return "T0d15LT6d15iT9d15vTfd15e"; // "Live"
	}
	
	/** This could be called when the tool is selected but not the case in practice. */
	@Override
	public void runMenuTool(String name, String command) { 
	}
	
	@Override
	public void runMacroTool(String name) {
	}
	
	/** React to right-click on the tool icon. */
	@Override
	public void showPopupMenu(MouseEvent e, Toolbar tb) {
	}

	/** Hack to do something when the tool is selected. */
	@Override
	public void eventOccurred(int eventID) {
		if (eventID == IJEventListener.TOOL_CHANGED && IJ.getToolName().equals(name)) {
			im.setMode("live");
		}		
	}

}