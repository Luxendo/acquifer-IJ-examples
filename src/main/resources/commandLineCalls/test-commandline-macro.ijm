/* 
 * The headless tag is optional.
 *
 * - Option 1 -macro
 * ImageJ-win64.exe --headless --console -macro Macro.ijm
 *
 * - Option 2 -scripts
 * ImageJ-win64.exe --ij2 --headless --console --run Macro.ijm
 */

// This one displays images and projection
// With -macro --headless, displaying is skipped
// With -macro but without the --headless, this trigger an issue if ImageJ was not already opened via the same command line 

// Make hyperstack
run("Make hyperstacks", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=[] z-slice(s)=[] timepoint(s)=[] display_stack project method=avg start=1 stop=3 show_projection output_directory=[]");

// Batch process hyperstacks - OK if not perfomring image-commands
//run("Batch process hyperstacks (macro)", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=[] z-slice(s)=[] timepoint(s)=[] display_stack method=avg start=1 stop=3 output_directory=[] default_directory=[] load_macro=[C:/Users/Laurent Thomas/OneDrive - ACQUIFER Imaging GmbH/SegmentUK/Lorenzo-ComparisonPlate//ComparisonPlate-SegmentBlob-FromBFstack-Variance.ijm] text1=print(getTitle());");

// Batch process script
// not recording

// BatchCopy - OK
//run("Batch Copy", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] output=[C:/Users/Laurent Thomas/Downloads/testCopy] including=[files only]");

// Batch Converter - OK
//run("Batch Converter", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] roi=[] scale=0.50 interpolation=Bilinear convert_to=JPEG output=[C:/Users/Laurent Thomas/Downloads/testCopy]");

// Bioformat Converter - OK
//run("Bioformat Converter", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] output_directory=[C:/Users/Laurent Thomas/Downloads/testBiof] use_companion filename=metadata including=[files only]");

// Batch process images
//run("Batch process images (macro)", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] default_directory=[] load_macro=[C:/Users/Laurent Thomas/Documents/github/acquifer/Fiji-examples/examples/Batch/ListImages/macro//printImagePath.ijm] text1=[imagePath = getArgument();\nprint(imagePath);]");

// Batch process images with macro extension - OK
//run("Batch process images (macro)", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] default_directory=[] load_macro=[C:/Users/Laurent Thomas/Documents/github/acquifer/Fiji-examples/examples/Batch/ListImages/macro//printImagePath.ijm] text1=[run(\"Acquifer IM04 macro extensions\");  \n\nfilename = \"-A002--PO01--LO001--CO6--SL001--PX32500--PW0080--IN0020--TM281--X023590--Y011262--Z211710--T0200262822--WE00002.tif\";\n\nprint(\"Image name :\", filename);\n\nID = Ext.getWellId(filename);\nprint(\"Well Id :\", ID);\n]");

// Batch process hyperstack maro with macro extension
//in = getArgument();
//print(in);
//run("Batch process hyperstacks (macro)", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 sub-position(s)=[] channel(s)=6 z-slice(s)=1 timepoint(s)=[] display_stack method=avg start=1 stop=3 output_directory=[] default_directory=[] load_macro=[C:/Users/Laurent Thomas/OneDrive - ACQUIFER Imaging GmbH/SegmentUK/Lorenzo-ComparisonPlate//ComparisonPlate-SegmentBlob-FromBFstack-Variance.ijm] text1=[run(\"Acquifer IM04 macro extensions\"); \015\n\015\nfilename =\"-A002--PO01--LO001--CO6--SL001--PX32500--PW0080--IN0020--TM281--X023590--Y011262--Z211710--T0200262822--WE00002.tif\";\015\n\015\nprint(\"\\n\" + filename);\015\n\015\nID = Ext.getWellId(filename);\015\nprint(\"Well Id :\", ID);\015\n\015\nExt.getWellColumn(filename, column);\015\nprint(\"Plate column : \", column);\015\n\015\nrow = Ext.getWellRow(filename);\015\nprint(\"Plate row : \", row);\015\n\015\nExt.getWellSubPosition(filename, subPos);\015\nprint(\"Well subposition : \", subPos);\015\n\015\nExt.getWellIndex(filename, index);\015\nprint(\"Well index (order of acquisition) : \", index);\015\n\015\nExt.getXYPosition(filename, X, Y);\015\nprint(\"Positions (mm) X: \", X, \" Y: \", Y);\015\n\015\nExt.getZPosition(filename, Z);\015\nprint(\"Position Z (mm) : \",Z);\015\n\015\nExt.getZSlice(filename, slice);\015\nprint(\"Z-slice : \", slice);\015\n\015\nExt.getLightPower(filename, power);\015\nprint(\"Light power (%) : \", power);\015\n\015\nExt.getLightExposure(filename, exposure);\015\nprint(\"Exposure time (ms) : \", exposure);\015\n\015\nExt.getChannelIndex(filename, channel);\015\nprint(\"Channel index : \", channel);\015\n\015\nExt.getObjectiveMagnification(filename, mag);\015\nprint(\"Objective Magnification (X) : \", mag);\015\n\015\nExt.getObjectiveNA(filename, NA);\015\nprint(\"Objective NA : \", NA);\015\n\015\nExt.getPixelSize(filename, pixSize); // this function also exists in ImageJ, hence the different text-color\015\nprint(\"Pixel Size (um) : \", pixSize);\015\n\015\nExt.getTimepoint(filename, timepoint);\015\nprint(\"Timepoint : \", timepoint);\015\n\015\nExt.getTemperature(filename, temp);\015\nprint(\"Temperature (C) : \", temp);]");