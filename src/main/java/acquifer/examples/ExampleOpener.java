package acquifer.examples;

import ij.IJ;
import ij.plugin.PlugIn;

import java.io.IOException;
import java.nio.file.*;
import java.nio.file.Path;
import java.nio.file.Paths;

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
		Path sourcePath = Paths.get(IJ.getDirectory("imagej"), "scripts", "Acquifer", "examples", subPath);
	    Path destPath   = Paths.get(IJ.getDirectory("temp"), sourcePath.getFileName().toString()); 
        try {
			Files.copy(sourcePath, destPath, StandardCopyOption.REPLACE_EXISTING); // overwrite previous temp file of same name
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		//File scriptFile = new File(filePath);
		//scriptFile.setReadOnly(); // prevent overwriting examples, not used anymore, was making the update show a disclaimer
		IJ.open(destPath.toString());
	}

}
