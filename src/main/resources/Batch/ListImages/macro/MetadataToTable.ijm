/*
 * This macro can be copy-pasted to the text field in the Batch (macro) plugin.
 * It reports in a table, the sucessive image paths of the images matching the dimensions selected in the Batch (macro) GUI.
 * As well as some metadata extracted from the filenames.
 * 
 * The Acquifer macro extension is used to parse the metadata from the filenames.
 * The succesive image paths are communicated from the Batch (macro) plugin to the macro as a String argument, via the getArgument() command.
 * 
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
 */

run("Acquifer IM04 macro extensions");  // this line is necessary to have access to the acquifer macro-functions via the Ext mechanism
//run("Acquifer IM03 macro extensions"); // uncomment this line for IM03

imagePath = getArgument();            // get image path for the current iteration from the Batch (macro) plugin
imageName = File.getName(imagePath);  // get filename from filepath

// Fill table row
newRowIndex = Table.size; // row index = table.size (because row indexes are 0-based, the latest row index in the table is size-1, hence the next one is size)
Table.set("Filepath", newRowIndex, imagePath);
Table.set("Well", newRowIndex, Ext.IM_getWellId(imageName));

Ext.IM_getLoopIteration(imageName, timepoint); // the value is returned in the variable timepoint
Table.set("Timepoint", newRowIndex, timepoint);

Ext.IM_getZSlice(imageName, slice);
Table.set("Z-index", newRowIndex, slice);

Ext.IM_getChannelIndex(imageName, channel);
Table.set("Channel", newRowIndex, channel);