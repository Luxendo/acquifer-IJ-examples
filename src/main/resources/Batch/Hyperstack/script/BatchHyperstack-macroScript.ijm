/*
 * This macro can be saved to disk and used as custom macro-file (.ijm) for the plugin "Batch process hyperstack (script)"
 * 
 * In this example, we just display the names of the stack and Z-projection (if any) to the log window. 
 * 
 * Like for other scripting languages, the macro should have 2 script parameters for the inputs (stack and proj as below), except that here the variable stack and proj correspond to the images names, not to ImagePlus objects.
 * These 2 inputs are necessary, even if no projection was done (in this case, proj is just null).
 * 
 * The script below works with or without a Z-projection, thanks to the "if (isOpen(imageID))" (see below).
 * Since the macro language functions are always executed on the currently active image, one uses selectImage(title) to select the image of interest (ie the stack or the projection).
 *
 * Contrary to other scripting languages, macros require to display the images, which is automatically done if an ijm script is provided, and displaying is not selected in the plugin interface. 
 * However, you can turn on the headless mode in your macro to process the images without systematically updating the display.
 * 
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
 */

// Every script/macro should have these 2 script-parameters, which get populated by the plugin.
#@ImagePlus stack
#@ImagePlus proj

print("\nNext stack...");

selectImage(stack);
getTitle(); // Example: get the title of the stack
// Other commands to process the stack

// proj might be null, if one didn't do a projection
// so we first check if the image is open
// This "if" can be removed if you know that a projection is done
// The block below can be completely removed if there is no Z-projection 
if (isOpen(proj)) { 
	selectImage(proj);
	getTitle(); // Example: get the title of the projection
	// Other commands to process the projection
}

// One can close the images after processing
print("Closing images...");
close("*");
