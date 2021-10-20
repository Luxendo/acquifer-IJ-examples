# acquifer-IJ-examples
 Dedicated jar package to populate the example and documentation entries of the ACQUIFER menu in Fiji.  
 The package basically contains a single-class which is responsible for opening the example scripts in the script editor.  
 There is then one entry in the ImageJ1 style plugins.config file, for each example script that should be listed in the menu.  
 
## Compilation  
While the jar package contains a single IJ1-type plugin, the package should be compiled with Maven.  
The example scripts are stored in the resource directory and listed accordingly in the plugins.config file (also part of the resource).  
The compilation will automatically put these script files in the jar, so they can be loaded in the code.  

In the maven configuration define the following properties to have the jar automatically copied to the Fiji.app/jars directory (thanks to the parent scijava pom)  
WARNING the jar is not copied to the plugin directory contrary to the other jar.  
Maybe this could be changed with the scijava.subdirectory parameters

Maven build parameters
scijava.app : Path to Fiji.app
enforcer.skip = true - this prevent issue since we have not filled all requirements of the parent pom (licences..)
scijava.deleteOtherVersions = older