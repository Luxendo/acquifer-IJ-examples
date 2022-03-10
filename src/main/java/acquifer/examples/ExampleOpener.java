package acquifer.examples;

import ij.plugin.PlugIn;
import net.imagej.legacy.IJ1Helper;

import java.net.URL;

import org.scijava.Context;
import org.scijava.ui.swing.script.TextEditor;

/** Open an example script in the script editor. <br>
 * It actually opens a temp copy of the script, to prevent overwriting the examples.<br>
 * This plugin can be used by adding a new entry for every example script in plugins.config, with the relative script path.<br>
 * The script path should be relative to Acquifer/examples.
 */
public class ExampleOpener implements PlugIn {
	
	/**
	 * @param subPath the filepath after Fiji.app/scripts/Acquifer/example.<br> For instance "macros\IM04\test-metadata-im04.ijm" 
	 */
	@Override
	public void run(String subPath) {
		URL url = getClass().getClassLoader().getResource(subPath);
		
		// Open a new instance of script editor
		// when opening multiple scripts over time would be nice to keep using the same instance
		Context context = IJ1Helper.getLegacyContext();
		TextEditor editor = new TextEditor(context);
		editor.loadTemplate(url); // name is not super adapted, not really a template, just loading from URL 
		editor.setVisible(true);  // displays it once script is loaded only
	}

}
