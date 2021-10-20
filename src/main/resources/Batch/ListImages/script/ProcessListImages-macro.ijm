/*
 * This macro can be saved to disk and used as custom macro-file (.ijm) for the plugin "Batch process images (script)"
 * 
 * In this example, we display the filepath to the image and open the image. 
 * 
 * Like for other scripting languages, the macro should have 1 script parameter of type File and named "image_file".
 * 
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/Fiji-examples
 */

#@ File image_file
print("\nProcess...")
print(image_file);

// Set batch mode to true (ie does not display opened images)
// Batch mode is thus usually faster at execution
//setBatchMode(true);

open(image_file);
run("Find Edges");

// wait 3 secs
print("Wait 3 seconds before closing image.");
wait(3000);
close();