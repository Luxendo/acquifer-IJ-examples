#@File (label="IM directory", style="directory") directory
//directory = "C:\\Users\\Laurent Thomas\\Documents\\Acquifer\\DataSet\\Hanh\\Lateral\\subSet4X" // or you manually pass a directory

run("Acquifer IM04 macro extensions");

selectedWell = newArray("B001", "B002"); // use upper case as in the filenames

selectedSubposition = newArray(1); // here 1 stands for the capacity of the array, not its content. we are thus creating an array to hold a single value.
selectedSubposition[0] = 1;        // we actually now store a value (1 but you could change it to other value) to the single "slot" in the array (which has index 0)

selectedChannels   = newArray(0);     // here we pass 0 to the size argument of the array, in effect creating an empty array. As a result, all available channels will be taken
selectedZ          = newArray(1,2,3); // with multiple values passed to new array, this directly stores the values in the array ie the array size is automatically adjusted to the number of values
selectedTimepoints = newArray(0);     // same for timepoints, by passing an empty array it will take all of them.


// This function will display at once all hyperstacks matching the selected dimensions
Ext.IM_showMultiHyperStacksFromDirectory(directory, selectedWell, 
                                         	     selectedSubposition, 
                                                 selectedChannels, 
                                                 selectedZ, 
                                                 selectedTimepoints); 

// This function display only a single hypertack
// this is convenient for looping, then you have the opportunity to process the generated hyperstacks before opening the next one
// Make sure to use upper case for the well ids ex: "A001"
// Here showing the first subposition within C002
Ext.IM_showSingleHyperStackFromDirectory(directory, "C002", 1, selectedChannels,
															selectedZ,
															selectedTimepoints);
