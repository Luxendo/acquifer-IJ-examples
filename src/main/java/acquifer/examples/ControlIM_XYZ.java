package acquifer.examples;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JOptionPane;

import ij.IJ;
import ij.gui.NonBlockingGenericDialog;
import ij.plugin.PlugIn;



/** 
 * A simple plugin that shows some control to move the XYZ axis of the IM.
 */
public class ControlIM_XYZ implements PlugIn, ActionListener {
	
	private NonBlockingGenericDialog dialog;
	
	@Override
	public void run(String arg) {

		dialog = new NonBlockingGenericDialog("IM control - Move objective to XYZ");
		
		dialog.addNumericField("X", 0);
		dialog.addToSameRow();
		dialog.addButton("Move X", this);
		
		dialog.addNumericField("Y", 0);
		dialog.addToSameRow();
		dialog.addButton("Move Y", this);
		
		dialog.addNumericField("Z", 0);
		dialog.addToSameRow();
		dialog.addButton("Move Z", this);
		
		dialog.showDialog();
	
		//JOptionPane.showMessageDialog(null, "Hello World"); // also works when calledfro mthe dropdown

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		double x = dialog.getNextNumber();	
		double y = dialog.getNextNumber();	
		double z = dialog.getNextNumber();
		
		dialog.resetCounters(); // to make sure the next "GUI reading" start again from the first field of the gui. See https://wsr.imagej.net/plugins/Button_Example2.java
		

		// directly use MoveXYZ in one go
		
	}

}
