# Examples for the ACQUIFER Java API  
Welcome to the example repository for the ACQUIFER Java API !  
This repo contains example jython scripts (.py) and ImageJ macros (.ijm), demonstrating classes available in the [ACQUIFER java packages](https://www.acquifer.de/resources/acquifer-java-packages/), and potential use cases.  
The examples are often designed for running in Fiji, although data types and classes under the acquifer.core package can be used in any Java programing environment (ICY, QuPath...). 
In Fiji, the java packages required to run these tests are shipped as part of the [ACQUIFER update site](https://www.acquifer.de/resources/acquifer-fiji-utilities/) in Fiji (freely available upon [request](https://www.acquifer.de/resources/acquifer-fiji-utilities/activate-update-site/)). The example scripts are also available after installation under the menu *Acquifer > Examples*.  

The example scripts can be found in the subdirectory [*src\main\resources*](https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources).
Or directly go to one of the example subsections : 
- [acquifer.core data-types](https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources/jython/Data-structure) (Dataset, ImagePlane...)
- [External microscope control via TcpIp](https://github.com/acquifer/acquifer-IJ-examples/tree/main/src/main/resources/jython/TcpIp)



## Download this repository
You can __download this repository__ by clicking the green button "code" and select "Download zip".  
Unzip the file, navigate to the subdirectory `src\main\resources` and drag and drop any of the script file on the Fiji toolbar to open it in the Fiji editor.  
Alternatively if you use GitHub, you can fork this repository to customize these examples to your need.  
You can also __download single files__ by clicking the filename, then the "raw" button at the top left of the page, and finally right-click, save as.  

## Documentation
You can find more documentation about the different ressources used in these examples on the following pages:
- [Metadata encoding](https://www.acquifer.de/metadata/) in image filenames
- [Batch-processing plugins](https://www.acquifer.de/fiji-batch-plugins/)
- [Processing individual image-files in batch](https://www.acquifer.de/batch-files/)
- [Hyperstack plugins](https://www.acquifer.de/hyperstack-fiji-plugins/)
- [Acquifer Java packages](https://www.acquifer.de/resources/acquifer-java-packages/)
- [acquifer-core](https://acquifer.github.io/acquifer-core/) java API documentation (compatible with any Java program)
- [acquifer-IJ](https://acquifer.github.io/acquifer-IJ/) java API documentation (custom scripting ressources for ImageJ/Fiji) 


## Compilation  
While the jar package contains a single IJ1-type plugin, the package should be compiled with Maven.  
The example scripts are stored in the resource directory and listed accordingly in the plugins.config file (also part of the resource).  
The compilation will automatically put these script files in the jar, so they can be loaded by the "Example launcher".  

In the maven configuration define the following properties to have the jar automatically copied to the Fiji.app/jars directory (thanks to the parent scijava pom).  

__Maven build parameters__  
scijava.app : Path to Fiji.app  
enforcer.skip = true - this prevent issue since the package does not fullfill all requirements of the parent pom (licences..)  
scijava.deleteOtherVersions = older  
