"""
From a list of images and associated metadatas, group images belonging to the same well positions
The result is a list containing one sublists per well subpositions.
A sublist contains the images belonging to a given well position
"""
#@ File (label="Dataset directory", style="directory") input_directory

from acquifer.core.im04 import FileUtils, Metadata

def printSubLists(mainList): 
	"""
	This function takes a list of list and print each item of the sublist  on a new line. 
	""" 
	for subList in mainList: 
		print "\n#Next subList" 
		 
		for item in subList: 
			print item 

utils = FileUtils()
input_directory = input_directory.getPath()
listMetadatas = utils.getListMetadatas(input_directory) # Get Metadata 
groupedImages = Metadata.groupByWellPositions(listMetadatas) 

printSubLists(groupedImages)