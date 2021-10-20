run("Acquifer IM03 macro extensions");
inputDir  = "C:/Users/Laurent Thomas/Documents/Acquifer/DataSet/Fish/IM03_BISCHOFF_DORSAL_2ndGO_4x";
//print (inputDir); //OK

Ext.getListImageFile(inputDir, listImage); // returning an array, here listImage is not implemented yet
Array.print(listImage);