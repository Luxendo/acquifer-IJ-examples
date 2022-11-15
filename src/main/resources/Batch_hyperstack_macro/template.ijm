/*
 * This macro can be copy/pasted in the custom macro field of the Batch Process Hyperstack (macro)
 * It simply prints the title of the image created at each iteration
 * 
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modifications.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
 */

// Print the images title
print("\nNext well/subposition");
imageTitle = getTitle();
print("title stack: ", imageTitle);

// Do some processing with the image