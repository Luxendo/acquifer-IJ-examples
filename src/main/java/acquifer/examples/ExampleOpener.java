package acquifer.examples;

import ij.IJ;
import ij.plugin.PlugIn;
import net.imagej.legacy.IJ1Helper;

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
		String url = getClass().getClassLoader().getResource(subPath).toString();
		String extension = url.substring(url.lastIndexOf(".") + 1);
		
		String language;
		switch(extension) {
			
		case("py"):
			language = "python";
			break;
		
		case("ijm"):
			language = "IJ1 Macro";
			break;
		
		default:
			throw new IllegalArgumentException("Currently implemented only for .py and .ijm files");
		}
		
		// Get the script editor
		Context context = IJ1Helper.getLegacyContext();
		TextEditor editor = new TextEditor(context);
		editor.setVisible(true);
		
		// Open a tab with the example
		editor.newTab(IJ.openUrlAsString(url),
					  language);
				
	}

}
