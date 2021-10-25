/*
 * This macro demonstrates how to parse the metadata from an image file name, for an image acquired with an Imaging Machine. 
 * You can directly run this macro, it is preconfigured with an example filename.
 * The metadata will be printed to a log window.
 * 
 * The first line loads the Acquifer macro extension, which allows calling the functions using the "Ext" mechanism.
 * 2 different macro extensions cannot be loaded simultaneously (if you need functionalities from another update site/package).
 * However, you can load another extension at the end of this script for instance, such that Ext will be refering to this new extension, and not to the Acquifer extension anymore.
 *
 * NOTE : When open via the menu ACQUIFER > Examples, this script file opens as a temporary file.
 * Changes to this file will thus NOT be saved, in particular the next time you open this example via the menu, the original example will be shown.
 * Use File > Save As... to save a copy of this example, and keep your modificationss.
 * You can also find all the examples on the following GitHub repository: https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources
 */

run("Acquifer IM04 macro extensions");  // this line is necessary to have access to the acquifer macro-functions via the Ext mechanism
//run("Acquifer IM03 macro extensions"); // uncomment this line for IM03

image_name = "-A002--PO01--LO001--CO6--SL001--PX32500--PW0080--IN0020--TM281--X023590--Y011262--Z211710--T0200262822--WE00002.tif";
//image_name = "WE00020---B005--PO01--LO001--CO6--SL010--PX16250--PW0040--IN0020--TM246--X050299--Y019906--Z212275--T1375574652.tif"; // uncomment this line for IM03

print("Image name :", image_name);

ID = Ext.IM_getWellId(image_name);
print("Well Id :", ID);

Ext.IM_getWellColumn(image_name, column);
print("Plate column : ", column);

row = Ext.IM_getWellRow(image_name);
print("Plate row : ", row);

Ext.IM_getWellSubPosition(image_name, subposition);
print("Well subposition : ", subposition);

Ext.IM_getWellIndex(image_name, well_index);
print("Well index (order of acquisition) : ", well_index);

Ext.IM_getXYPosition(image_name, x_mm, y_mm);
print("Positions (mm) X: ", x_mm, " Y: ", y_mm);

Ext.IM_getZPosition(image_name, z_mm);
print("Position Z (mm) : ", z_mm);

Ext.IM_getZSlice(image_name, z_slice);
print("Z-slice : ", z_slice);

Ext.IM_getLightPower(image_name, light_power);
print("Light power (%) : ", light_power);

Ext.IM_getLightExposure(image_name, light_exposure);
print("Exposure time (ms) : ", light_exposure);

Ext.IM_getChannelIndex(image_name, channel);
print("Channel index : ", channel);

Ext.IM_getPixelSize(image_name, pixel_size_um); // this function also exists in ImageJ, hence the different text-color
print("Pixel Size (um) : ", pixel_size_um);

Ext.IM_getTimepoint(image_name, timepoint);
print("Timepoint : ", timepoint);

Ext.IM_getTemperature(image_name, temperature);
print("Temperature (°C) : ", temperature);