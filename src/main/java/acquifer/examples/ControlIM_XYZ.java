package acquifer.examples;

import java.awt.Button;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JOptionPane;

import acquifer.core.TcpIp;
import ij.IJ;
import ij.gui.NonBlockingGenericDialog;
import ij.plugin.PlugIn;



/** 
 * A simple plugin that shows some control to move the XYZ axis of the IM.
 */
public class ControlIM_XYZ implements PlugIn, ActionListener {
	
	private NonBlockingGenericDialog dialog;
	
	private String LABEL_MOVE_XY = "Move XY";
	private String LABEL_MOVE_Z = "Move Z";
	
	private TcpIp im;
	
	@Override
	public void run(String arg) {
		
		try { 
			im = new TcpIp(); // open the communication port with the IM
		}
		
		catch (Exception error) {
			IJ.error(error.getMessage());
			error.printStackTrace();
			return; 
		}
		
		
		dialog = new NonBlockingGenericDialog("IM control - Move objective to XYZ");
		
		dialog.addNumericField("X (mm)", im.getPositionX());
		dialog.addNumericField("Y (mm)", im.getPositionY());
		dialog.addToSameRow();
		dialog.addButton(LABEL_MOVE_XY, this);
		
		dialog.addNumericField("Z (µm)", im.getPositionZ());
		dialog.addToSameRow();
		dialog.addButton(LABEL_MOVE_Z, this);
		
		dialog.hideCancelButton();
		dialog.showDialog();
	
		//JOptionPane.showMessageDialog(null, "Hello World"); // also works when called from the dropdown

	}

	@Override
	public void actionPerformed(ActionEvent e) {
		
		double x = dialog.getNextNumber();	
		double y = dialog.getNextNumber();	
		double z = dialog.getNextNumber();
		
		dialog.resetCounters(); // to make sure the next "GUI reading" start again from the first field of the gui. See https://wsr.imagej.net/plugins/Button_Example2.java
		
		Button button = (Button) e.getSource();
		String label = button.getLabel();
		
		if (label == LABEL_MOVE_XY)
			im.moveXYto(x, y);
		
		else
			im.moveZto(z);
		
	}

		
}


