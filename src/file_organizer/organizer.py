#os module -> for the interaction with the OS
import os
#directory path stored in string
path = "/Users/hazee/Documents/Test"
#get names of files and folders
#order not guaranteed
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
#display names of files and folders
print(dir_list)