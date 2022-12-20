import getfilepath

# You will have to input the name of a connected drive you want to search, or else it will take the default drive —>
# “C:\\“.
getfilepath.driveName = "D://"

# We can use the fileaccess module to find out where the files are located in memory and return a file path for a given filename.
print(getfilepath.returnFilepath("balaji"))

# This will return a count of parameter names with extensions.
print(getfilepath.extensionCounter("balaji", ".png"))

# We will also return the number of the given filename in memory.
print(getfilepath.fileNameCounter("balaji"))

# The file name in the given parameter extension is returned.
print(getfilepath.nameWithExtension("balaji", ".png"))

# This function will open a file with only passing its name.
print(getfilepath.openFileWithName("balaji"))