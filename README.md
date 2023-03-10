Access With Name is a  file access module to find out where the files are located in memory and return a file path for a given filename. We will also return a count of the given filename in memory.

pip install getfilepath

Source code available at https://github.com/SriBalaji2112/GetFilePath/documentation

https://github.com/SriBalaji2112/GetFilePath

If you need help installing Python, visit https://installpython3.com/



.. Access With Name documentation master file, created by
   Balaji on Tuesday Dec 20 10.00.00 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `GetFilePath` directive.

Welcome to getfilepath's documentation!
=====================================


We can use the fileaccess module to find out where the files are located in memory and return a file path for a given filename. We will also return a count of the given filename in memory.

This function will count how many given external files are in your memory and return it.
You must enter a drive name, which drive you want to search.
The API is designed to be simple. GetFilePath works on Windows, macOS, and Linux, and runs on Python 2 and 3.

To install with pip, run ``pip install GetFilePath``. See the :doc:`install` page for more details.

The source code is available on: https://github.com/SriBalaji2112/GetFilePath

GetFilePath has several features:

* It will return the file path for the given filename and file type.
* ExtensionsCounter counts the number of files in a specific extension.
* This service will return the full file path of a given file name.
* This function will count how many given external files are in your memory and return it.

Examples
========

.. code :: python

Example Testing Program and function definition

    >>> import GetFilePath

    >>> # You will have to input the name of a connected drive you want to search, or else it will take the default drive —> “C:\\“.
    >>> GetFilePath.driveName = "D://"

    >>> # We can use the fileaccess module to find out where the files are located in memory and return a file path for a given filename.
    >>> print(GetFilePath.returnFilepath("balaji"))

    >>> # This will return a count of parameter names with extensions.
    >>> print(GetFilePath.extensionCounter("balaji", ".png"))

    >>> # We will also return the number of the given filename in memory.
    >>> print(GetFilePath.fileNameCounter("balaji"))

    >>> # The file name in the given parameter extension is returned.
    >>> print(GetFilePath.nameWithExtension("balaji", ".png"))

    >>> # This function will open a file with only passing its name.
    >>> print(GetFilePath.openFileWithName("balaji"))


Output of the testing program

.. code :: python

    >>>  ['D://Attedance project 2.0/balaji2.png', 'D://Attedance project 2.0/images/BALAJI S.jpg', 'D://Attedance project 2.0/img/balaji.png', 'D://Attedance project 2.0/img/balaji3.png', 'D://College/Updated/BALAJI B.jpg', 'D://image compare/balaji2.png', 'D://image compare/img/balaji - Copy (2).png', 'D://image compare/img/balaji - Copy (3).png', 'D://image compare/img/balaji - Copy (4).png', 'D://image compare/img/balaji - Copy (5).png', 'D://image compare/img/balaji - Copy (6).png', 'D://image compare/img/balaji - Copy (7).png', 'D://image compare/img/balaji - Copy.png', 'D://image compare/img/balaji.png', 'D://image compare/img/balaji3.png', 'D://pycham/Attedance project 2.0/images/BALAJI S.jpg', 'D://pycham/attedence project/images/BALAJI S.jpg']
    >>>  13
    >>>  17
         ['D://Attedance project 2.0/balaji2.png', 'D://Attedance project 2.0/img/balaji.png', 'D://Attedance project 2.0/img/balaji3.png', 'D://image compare/balaji2.png', 'D://image compare/img/balaji - Copy (2).png', 'D://image compare/img/balaji - Copy (3).png', 'D://image compare/img/balaji - Copy (4).png', 'D://image compare/img/balaji - Copy (5).png', 'D://image compare/img/balaji - Copy (6).png', 'D://image compare/img/balaji - Copy (7).png', 'D://image compare/img/balaji - Copy.png', 'D://image compare/img/balaji.png', 'D://image compare/img/balaji3.png']
         1  -- balaji2.png
         2  -- BALAJI S.jpg
         3  -- balaji.png
         4  -- balaji3.png
         5  -- BALAJI B.jpg
         6  -- balaji2.png
         7  -- balaji - Copy (2).png
         8  -- balaji - Copy (3).png
         9  -- balaji - Copy (4).png
         10  -- balaji - Copy (5).png
         11  -- balaji - Copy (6).png
         12  -- balaji - Copy (7).png
         13  -- balaji - Copy.png
         14  -- balaji.png
         15  -- balaji3.png
         16  -- BALAJI S.jpg
         17  -- BALAJI S.jpg
         They are  17 files in this name, choose your file: 
         Say a exact file.
         Enter a file name: 2
         Opening a File  D://Attedance project 2.0/images/BALAJI S.jpg
         File Open successfully.


The benefit of using GetFilePath, Easily access a file with only file name.


FAQ: Frequently Asked Questions
===============================

Send questions to https://github.com/SriBalaji2112