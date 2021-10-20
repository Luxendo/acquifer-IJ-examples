/*
 * This simple macro can be copy-pasted to the text field in the Batch (macro) plugin.
 * It simply prints to the log window, the sucessive image paths of the images matching the dimensions selected in the Batch (macro) GUI.
 * NOTE : The filepaths in the log window can be clicked to directly open the images in Fiji !
 * You can save the content of this log window to a text file and open it later again in a text editor or in Fiji.
 * 
 * The image path is communicated from the Batch (macro) plugin to the macro as a String argument, which can be recovered using the getArgument() command.
 * 
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
 */

imagePath = getArgument(); // get image path for the current iteration of the Batch (macro) plugin
print(imagePath);