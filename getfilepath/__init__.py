# Python Search or open a file with given filename.
# It's also give a file path with or without file Extension.  <======

# on Python 3 and 2.

# BJ SriBalaji sribalaji2112@gmail.com (Send me feedback & suggestions!)    <-------
# MIT license

# TODO - Follow https://github.com/SriBalaji2112

# ---->  github.com/SriBalaji2112  <-----
# Python Program for Accessing a File with in a Second

import os  # For Opening a File

driveName = "C://"

def drive(d):
    global driveName
    if "://" in d:
        driveName = d
    else:
        driveName = d + "://"


def openFileWithName(filename):  # Open a file with only using file name.
    global driveName

    def word_num(choice):  # If search file are have more then one result the choice which appear.
        help_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0',
            'first': '1',
            'second': '2',
            'third': '3',
            'forth': '4',
            'fifth': '5',
            'sixth': '6',
            'seventh': '7',
            'eighth': '8',
            'ninth': '9',
            'zeroth': '0'
        }
        res = help_dict[choice]
        return res

    def file_acces(f):  # File Opener.
        os.startfile(f)  # OS module has open a file with using file path
        print("Opening a File ", f)
        print("File Open successfully.")

    def opener(filename):  # opener function will do open a file with using file name,
        global driveName
        try:
            filename.lower()

            if len(filename) >= 1:
                dir_path = os.path.dirname(driveName)
                ''' give a Disk Name and
                In OS module have dirname into the path function to get the all file path.'''
                for root, dirs, files in os.walk(
                        dir_path):  # os.walk function is split the path into root, dirs, files.
                    for file in files:
                        lower_file_name = file.lower()
                        if filename in lower_file_name:  # Check File name in your Given Input
                            # more_path += 1
                            f = root + '\\' + str(file)
                            f = f.replace("\\", "/")

                            current_file.append(f)
                            current_str.append(file)
                            # os.startfile(f)  # Open a File

            # print(more_path)

        except Exception as E:  # In case if any Error the Exception will handle that.
            print(E)

    current_str = []
    current_file = []  # current file is list array formate.

    opener(filename)

    for i in range(1, len(current_file) + 1):
        print(i, "--".center(3), current_str[i - 1])

    if len(current_file) > 1:
        print("They are ", len(current_file), "files in this name, choose your file: ")

        print("Say a exact file.")
        choice = input("Enter a file name: ")
        choice.lower()
        try:  # In this statement check the result file path is more then one.
            try:
                if type(choice) == str:
                    choice = int(word_num(choice))
                    print(choice)
                    file_acces(current_file[choice - 1])
            except:
                choice = int(choice)
                file_acces(current_file[choice - 1])
        except:
            for i in range(len(current_str)):
                str_choice = current_str[i].lower()
                if choice in str_choice:
                    file_acces(current_file[i])
    elif len(current_file) == 1:
        for c_file in current_file:
            file_acces(c_file)
    else:
        print("No File are in your disk")


def returnFilepath(filename):  # This function will return the full file path of a given file name
    global driveName
    try:

        current_str = []
        current_file = []

        filename.lower()

        if len(filename) >= 1:
            dir_path = os.path.dirname(driveName)  # Disk Name
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    lower_file_name = file.lower()
                    if filename in lower_file_name:  # Check File name in your Given Input
                        # more_path += 1
                        f = root + '\\' + str(file)
                        f = f.replace("\\", "/")

                        current_file.append(f)
                        current_str.append(file)
                        # os.startfile(f)  # Open a File

        return current_file

        # print(more_path)

    except Exception as E:  # In case if any Error the Exception will handle that.
        print(E)


def nameWithExtension(filename, filetype):  # pathWithExtension will get a two attribute 'filename' and 'filetype'.
    # It will return the file path for the given filename and filetype.
    global driveName
    try:
        def fileAccess(filename, filetype):
            current_str = []
            current_file = []

            filename.lower()

            if len(filename) >= 1:
                dir_path = os.path.dirname(driveName)  # Disk Name
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        s_letter = file.lower()
                        if filename in s_letter:
                            f = root + '\\' + str(file)
                            f = f.replace("\\", "/")
                            if file.endswith(filetype):
                                current_file.append(f)
                                current_str.append(file)
                            # os.startfile(f)  # Open a File

            return current_file

        if '.' in filetype:  # It will check the given Extension will have '.' or not.
            return fileAccess(filename, filetype)

        else:  # If the dot is not in given Filetype it will add the '.' in front of given filetype.
            c_filetype = '.' + filetype
            return fileAccess(filename, c_filetype)

        # print(more_path)

    except Exception as E:  # In case if any Error the Exception will handle that.
        print(E)


def fileNameCounter(filename):
    global driveName
    counter = 0
    dir_path = os.path.dirname(driveName)  # Disk Name
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            s_letter = file.lower()
            if filename in s_letter:
                f = root + '\\' + str(file)
                f = f.replace("\\", "/")
                counter += 1
    return counter


def extensionCounter(filename, filetype):  # ExtensionsCounter counts and return the number of files in a specific extension.
    global driveName
    counter = 0
    dir_path = os.path.dirname(driveName)  # Disk Name
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            s_letter = file.lower()
            if filename in s_letter:
                f = root + '\\' + str(file)
                f = f.replace("\\", "/")
                if file.endswith(filetype):
                    counter += 1
    return counter

#  github.com/SriBalaji2112
#  Thanks For visiting My GitHub page.
