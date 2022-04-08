/*
 * This macro can be copy-pasted to the text field in the Batch (macro) plugin.
 * It provides a template, for the execution of custom macro-commands on the successive images as selected in the Batch (macro) plugin.
 * 
 * The image path is communicated from the Batch (macro) plugin to the macro as a String argument, which can be recovered using the getArgument() command.
 * The image is then opened (and displayed if BatchMode is not set to true).
 * Custom commands are executed and the image is closed.
 * 
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
 */
imagePath = getArgument();

//setBatchMode(true); // In batch-mode, images are not displayed to speed up processing. Ucomment this line to activate the batch mode
open(imagePath);     // if BatchMode is not set to true, this will display the image

// Execute some commands ex: edge detection
run("Mean...", "radius=2"); // smooth before edge detection to reduce noise
run("Find Edges");
run("Enhance Contrast", "saturated=0.35");

wait(2000); // wait 2 secs before closing

// Close image after execution (in batch mode, this frees the image memory)
close("*"); // Comment this line with // to keep images opened (if batch mode is not true)