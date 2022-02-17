# Controlling the IM via external java applications
This subdirectory contains example snippets demonstrating how to use an external java application (ex: Fiji) to control the Imaging Machine via the TcpIp protocol.  
No knowledge of the TcpIp protocol is necessary, the functions are available as part of the acquifer-core java package.  
This package is shipped with the acquifer update site in Fiji, but can be used with any java application (QuPath, ICY...).  

The commands in the acquifer-core package are illustrated here with the jython scripting language, which can be directly used in Fiji.  
Any other language supported by the Java Virtual Machine (Groovy...) ca be used, one just needs to adapt the syntax accordingly.  

NOTE : the commands communicate with the software of the Imaging Machine, not with the microscope directly.  
The software should thus be opened before opening the communication port, and the option "Block remote access" in the service panel deactivated (restart of the software needed to take effect).  
Refer to the acquifer-core API documentation for more information about the individual functions.  