package acquifer.toolbarIM;

import java.awt.EventQueue;
import java.awt.MenuItem;
import java.awt.PopupMenu;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;

import javax.swing.JOptionPane;

import acquifer.core.TcpIp;
import acquifer.examples.ControlIM_XYZ;
import ij.IJ;
import ij.IJEventListener;
import ij.gui.Toolbar;
import ij.plugin.tool.PlugInTool;

/** This menu is made to be right-click. The dropdown menu provide menu entries which executes action on click.
 * This plugin is in a way a workaround to the impossibility to make java equivalent of the macro-based Action Tool, i.e that just do stuff when clicked..*/
public class DropdownIM extends PlugInTool implements IJEventListener, ActionListener {
	
	private TcpIp im;
	private String name = "IM actions";
	
	public DropdownIM(TcpIp im){
		this.im = im;
		IJ.addEventListener(this); // the plugin will get notified by ImageJ for IJevent, this was to react to tool switches
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
		return "T1d15IT4d15M"; // IM font size 15, x = 1, y = 13 i.e d in hex, see https://imagej.nih.gov/ij/developer/macro/macros.html#icons
	}
	
	/** This could be called when the tool is selected but not the case in practice. */
	@Override
	public void runMenuTool(String name, String command) { 
	}
	
	@Override
	public void runMacroTool(String name) {
	}
	
	/** Show theright click menu and defines what happen when one menu is clicked */
	@Override
	public void showPopupMenu(MouseEvent e, Toolbar tb) {
		
		PopupMenu dropdown = new PopupMenu();
		
		// Set to live mode
		MenuItem setLiveMenu = new MenuItem("Switch live mode");
		setLiveMenu.setActionCommand("live");
		setLiveMenu.addActionListener(this);
		dropdown.add(setLiveMenu);
		
		// Open/Close lid
		MenuItem openCloseMenu = new MenuItem("Open/Close lid");
		openCloseMenu.setActionCommand("lid");
		openCloseMenu.addActionListener(this);
		dropdown.add(openCloseMenu);
		
		/*
		// Move IM XYZ
		// Open/Close lid
		MenuItem moveIM_Menu = new MenuItem("Move objective (XYZ)");
		moveIM_Menu.setActionCommand("move");
		moveIM_Menu.addActionListener(this);
		dropdown.add(moveIM_Menu);
		*/
		
		// Add dropdown to toolbar before showing it
		tb.add(dropdown);
		dropdown.show(e.getComponent(), e.getX(), e.getY());
	}

	/** Hack to do something when the tool is selected. */
	@Override
	public void eventOccurred(int eventID) {
		/*
		if (eventID == IJEventListener.TOOL_CHANGED && IJ.getToolName().equals(name)) {
			im.setMode("live");
		}
		*/		
	}

	@Override
	/** Handles the clicks in the right click menu */
	public void actionPerformed(ActionEvent e) {
		
		switch(e.getActionCommand()) {
			
			case "live":
				im.setMode("live");
				break;
			
			case "lid":
				
				if (im.isLidClosed())
					im.openLid();
				else
					im.closeLid();
				
				break;
			
			case "move": // never happening, commented above
				/*trying to call the plugin just freezes, some threading issue
				EventQueue.invokeLater(new Runnable() {
				    public void run() {
						ControlIM_XYZ plugin = new ControlIM_XYZ();
						plugin.run("");
						IJ.log("finished calling plugin");
				    }
				});
				*/
				JOptionPane.showMessageDialog(null, "Hello World"); // works

				break;
		}
	}

}