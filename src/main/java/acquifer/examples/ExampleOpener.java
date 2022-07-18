package acquifer.examples;

import ij.plugin.PlugIn;
import net.imagej.legacy.IJ1Helper;

import java.net.URL;

//import org.apache.commons.io.FilenameUtils;
import org.fife.ui.rsyntaxtextarea.SyntaxConstants;
import org.scijava.ui.swing.script.TextEditor;

/** Open an example script in the script editor. <br>
 * It actually opens a temp copy of the script, to prevent overwriting the examples.<br>
 * This plugin can be used by adding a new entry for every example script in plugins.config, with the relative script path.<br>
 * The script path should be relative to Acquifer/examples.
 */
public class ExampleOpener implements PlugIn {
	
	/** Single instance of the text editor, to avoid opening a new one each time. */
	private static TextEditor editor = new TextEditor(IJ1Helper.getLegacyContext());
	
	/**
	 * @param subPath the filepath after Fiji.app/scripts/Acquifer/example.<br> For instance "macros\IM04\test-metadata-im04.ijm" 
	 */
	@Override
	public void run(String subPath) {
		URL url = getClass().getClassLoader().getResource(subPath);
		
		editor.loadTemplate(url); // name is not super adapted, not really a template, just loading from URL 
		
		// Workaround to set syntax highlighting for C#, and more generally non scripting languages
		// https://forum.image.sc/t/texteditor-setlanguage-for-other-file-formats/69569/2?u=lthomas
		if (subPath.endsWith(".cs")) {
			editor.getTextArea().setSyntaxEditingStyle(SyntaxConstants.SYNTAX_STYLE_CSHARP);
			//editor.setEditorPaneFileName(FilenameUtils.getBaseName(subPath)); // does not help, still the extension of the last used scripting language
			// actually last commented line even cause trouble upon opening a second tab
		}
		
		editor.setVisible(true);  // displays it once script is loaded only, or if already shown bring to front
	}

}
