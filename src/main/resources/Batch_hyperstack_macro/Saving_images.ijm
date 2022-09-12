/**
 * This macro demonstrates different options to save an image at different locations when using the batch macro plugins:  
 * - option1: Saving in the image directory
 * - option2: Saving in the default subdirectory within the image directory
 * - option3: Saving in a custom directory (here chosen as a custom subdirectory within the image directory)
 * Here the active image is saved as tiff, although the code could be adapted to save an image after some pre-processing, and with a different extension (simply change the extension in the code below).
 */
 
imageDir = getDirectory("image"); // recover current image directory (terminated by the default platform path separator)
imageName = getTitle() + "-proc"; // we save the image as orignal name + "-proc"
extension = "tif"; // can be replaced by "jpeg", "png"...

// Option1 :  Directly save in the current dataset directory, next to the original images (not recommended, better save in a dedicated directory)
imagePath = imageDir + imageName;
print("\nSaving in image directory...");
print(imagePath + "." + extension);
saveAs(extension, imagePath);


// Option2 : Save in the default subdirectory of the current image dataset
// This options has the advantage that the directory is automatically created by the batch plugin for you
// You can specify the default directory in the batch plugin interface
// if the filed is left empty, the default subdirectory is "macro_output" within the image directory
defaultDir = getDirectory("default");
imagePath2 = defaultDir + imageName;
print("\nSaving in default subdirectory...");
print(imagePath2 + "." + extension);
saveAs(extension, imagePath2);


// Option3 : Save in a custom directory, here a custom subdirectory within the current image dataset
// This is the most flexible option, if you need to save different types of data in different subdirectories 
// in this case the default directory nmight not be sufficient (although you can combine both approaches)
// Here, we have to make sure a directory exist before saving files into it, otherwise we will get an IOerror upon saving
// We create the directory if not existing
subDirectory = imageDir + "out"; // ie we save in a subdirectory "out" within the image directory 

// Check if the subdirectory exists, if not create it
if (! File.exists(subDirectory)) {
	File.makeDirectory(subDirectory);
}

imagePath3 = subDirectory + File.separator + imageName; // dont forget the file separator (automatically resolves to / or \ depending on the OS)
print("\nSaving in custom subdirectory...");
print(imagePath3 + "." + extension);
saveAs(extension, imagePath3);

print("\nClick the filepaths above to directly open the file in Fiji.")