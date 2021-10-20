/* 
 * The headless tag is optional.
 *
 * - Option 1 -macro
 * ImageJ-win64.exe --headless --console -macro Macro2.ijm
 *
 * - Option 2 -scripts
 * ImageJ-win64.exe --ij2 --headless --console --run Macro2.ijm
 */

// This one displays images and projection
// With -macro --headless, displaying is skipped
// With -macro but without the --headless, this trigger an issue if ImageJ was not already opened via the same command line 
run("Make hyperstacks", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf_Offset] c002 c003 sub-position(s)=[] channel(s)=[] z-slice(s)=[] timepoint(s)=[] display_stack project method=avg start=1 stop=3 show_projection output_directory=[]");

// This next one does not display but saves projection on disk
//run("Make hyperstacks", "directory=[C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Hanh/Lateral/Lateral_Live_20X_RFp_GFP_Stack10um_2dpf] c002 c003 sub-position(s)=[] channel(s)=[] z-slice(s)=[] timepoint(s)=[] project method=max start=2 stop=9 save_projection output_directory=[C:/Users/Laurent Thomas/Downloads/outmacro]");
