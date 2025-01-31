# To list all files and folders recursively from a given directory path, you can use the os 
# and os.walk() modules in Python.

# Python Code to Print All Files & Folder Paths

import os

def list_files_and_folders(directory):
    for root, dirs, files in os.walk(directory):
        for folder in dirs:
            print(os.path.join(root, folder))  # Print folder path
        for file in files:
            print(os.path.join(root, file))  # Print file path

# Example Usage
directory = "/Users/name/Desktop/folder"  # Change this to your target directory
list_files_and_folders(directory)

# # output
# /Users/name/Desktop/folder/subfolder1
# /Users/name/Desktop/folder/subfolder2
# /Users/name/Desktop/folder/subfolder1/file1.txt
# /Users/name/Desktop/folder/subfolder1/file2.jpg
# /Users/name/Desktop/folder/file3.pdf

# How It Works?
# os.walk(directory) traverses the directory recursively.
# root → Current directory.
# dirs → List of directories inside root.
# files → List of files inside root.
# os.path.join(root, item) constructs the full path for each file and folder.

# Alternative: Using Pathlib (Python 3.5+)
from pathlib import Path

def list_all_paths(directory):
    for path in Path(directory).rglob('*'):  # Recursively find all paths
        print(path)

# Example Usage
directory = "/Users/name/Desktop/folder"
list_all_paths(directory)

# 🚀 Use os.walk() for full control and Pathlib for a cleaner solution! ✅








