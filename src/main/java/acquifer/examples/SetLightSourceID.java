package acquifer.examples;

import ij.Prefs;
import ij.gui.GenericDialog;
import ij.plugin.PlugIn;



/** 
 * This is a configuration plugin for the plugin MoveIMToClik to specify custom led names in the gui.
 */
public class SetLightSourceID implements PlugIn {
	
	@Override
	public void run(String arg) {
		
		GenericDialog dialog = new GenericDialog("Set light source labels for 'Move IM to click'");
		
		dialog.addStringField("led1", Prefs.get("lightsource.led1", "led1"));
		dialog.addStringField("led2", Prefs.get("lightsource.led2", "led2"));
		dialog.addStringField("led3", Prefs.get("lightsource.led3", "led3"));
		dialog.addStringField("led4", Prefs.get("lightsource.led4", "led4"));
		dialog.addStringField("led5", Prefs.get("lightsource.led5", "led5"));
		dialog.addStringField("led6", Prefs.get("lightsource.led6", "led6"));


		dialog.hideCancelButton();
		dialog.showDialog();
		
		if (dialog.wasOKed()) {
			Prefs.set("lightsource.led1", dialog.getNextString());
			Prefs.set("lightsource.led2", dialog.getNextString());
			Prefs.set("lightsource.led3", dialog.getNextString());
			Prefs.set("lightsource.led4", dialog.getNextString());
			Prefs.set("lightsource.led5", dialog.getNextString());
			Prefs.set("lightsource.led6", dialog.getNextString());
		}

	}


		
}


