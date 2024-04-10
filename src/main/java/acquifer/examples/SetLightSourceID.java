package acquifer.examples;

import java.awt.Button;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JOptionPane;

import acquifer.core.TcpIp;
import ij.IJ;
import ij.Prefs;
import ij.gui.GenericDialog;
import ij.gui.NonBlockingGenericDialog;
import ij.plugin.PlugIn;



/** 
 * A simple plugin that shows some control to move the XYZ axis of the IM.
 */
public class SetLightSourceID implements PlugIn {
	
	@Override
	public void run(String arg) {
		
		GenericDialog dialog = new GenericDialog("Set light source labels for 'Move IM to click'");
		
		dialog.addStringField("Fluo1", Prefs.get("lightsource.fluo1", "Fluo1"));
		dialog.addStringField("Fluo2", Prefs.get("lightsource.fluo2", "Fluo2"));
		dialog.addStringField("Fluo3", Prefs.get("lightsource.fluo3", "Fluo3"));
		dialog.addStringField("Fluo4", Prefs.get("lightsource.fluo4", "Fluo4"));
		dialog.addStringField("Fluo5", Prefs.get("lightsource.fluo5", "Fluo5"));

		dialog.hideCancelButton();
		dialog.showDialog();
		
		if (dialog.wasOKed()) {
			Prefs.set("lightsource.fluo1", dialog.getNextString());
			Prefs.set("lightsource.fluo2", dialog.getNextString());
			Prefs.set("lightsource.fluo3", dialog.getNextString());
			Prefs.set("lightsource.fluo4", dialog.getNextString());
			Prefs.set("lightsource.fluo5", dialog.getNextString());
		}
		//JOptionPane.showMessageDialog(null, "Hello World"); // also works when called from the dropdown

	}


		
}


