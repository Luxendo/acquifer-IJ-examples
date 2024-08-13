package acquifer.examples;

import ij.Prefs;
import ij.gui.GenericDialog;
import ij.plugin.PlugIn;



/** 
 * This is a configuration plugin for the plugin MoveIMToClik to specify custom led names and filters in the plugin's gui.
 */
public class SetLightSourceID implements PlugIn {
	
	@Override
	public void run(String arg) {
		
		GenericDialog dialog = new GenericDialog("Set light source labels for 'Move IM to click'");
		
		// LEDs (6 in total)
		dialog.addStringField("led1", Prefs.get("lightsource.led1", "led1"));
		dialog.addStringField("led2", Prefs.get("lightsource.led2", "led2"));
		dialog.addStringField("led3", Prefs.get("lightsource.led3", "led3"));
		dialog.addStringField("led4", Prefs.get("lightsource.led4", "led4"));
		dialog.addStringField("led5", Prefs.get("lightsource.led5", "led5"));
		dialog.addStringField("led6", Prefs.get("lightsource.led6", "led6"));
		
		// Filters (5 in total)
		dialog.addStringField("Filter 1", Prefs.get("filtercube.1", "1"));
		dialog.addStringField("Filter 2", Prefs.get("filtercube.2", "2"));
		dialog.addStringField("Filter 3", Prefs.get("filtercube.3", "3"));
		dialog.addStringField("Filter 4", Prefs.get("filtercube.4", "4"));
		dialog.addStringField("Filter 5", Prefs.get("filtercube.5", "5"));


		dialog.hideCancelButton();
		dialog.showDialog();
		
		if (dialog.wasOKed()) {
			
			Prefs.set("lightsource.led1", dialog.getNextString());
			Prefs.set("lightsource.led2", dialog.getNextString());
			Prefs.set("lightsource.led3", dialog.getNextString());
			Prefs.set("lightsource.led4", dialog.getNextString());
			Prefs.set("lightsource.led5", dialog.getNextString());
			Prefs.set("lightsource.led6", dialog.getNextString());
			
			Prefs.set("filtercube.1", dialog.getNextString());
			Prefs.set("filtercube.2", dialog.getNextString());
			Prefs.set("filtercube.3", dialog.getNextString());
			Prefs.set("filtercube.4", dialog.getNextString());
			Prefs.set("filtercube.5", dialog.getNextString());
		}

	}


		
}


