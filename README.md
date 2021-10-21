# acquifer-IJ-examples
Example macros (.ijm) and jython scripts (.py) demonstrating useful functions provided by the [ACQUIFER update site](https://www.acquifer.de/resources/acquifer-fiji-utilities/) in Fiji (freely available upon [request](https://www.acquifer.de/resources/acquifer-fiji-utilities/activate-update-site/)), or more generally by the [ACQUIFER java packages](https://www.acquifer.de/resources/acquifer-java-packages/).  
The example scripts can be found in the subdirectory `src\main\resources` of this repository.  
These examples are also shipped by the update site, and are available in the menu *Acquifer > Examples*.  

Currently for the ImageJ macro-language, the examples cover the extraction of metadata from the image file name (see *examples > MetadataParsing*).  

The jython scripts demonstrate a larger panel of functions available in the Java API, which can be reproduced in other scripting languages supported by Fiji.  
For the scripting examples, some functions are specifically available for Fiji (ex: hyperstack), while others such as metadata parsing are not depending on Fiji and thus could be used in other java software such as QuPath or ICY.

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
### (for us when we make this package)   
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
