import os
import re

# Define the paths for the trash files and info directory
path = "/home/lenovo/.local/share/Trash/files"
infopath = "/home/lenovo/.local/share/Trash/info"

# List of files in the Trash folder
dirlist = os.listdir(path)
directory = []  # List to hold the filenames
popis = ""

# Iterate through the files in the Trash
for fname in dirlist:
    directory.append(fname)
    popis = popis + " " + fname  # Build a string of file names for display

# Print the list of files
print(popis)

# Ask the user to enter the file name to recover
fname = input("\nEnter the file name which you want to recover: ")

# Open the corresponding .trashinfo file for the selected file
a = open(infopath + "/" + fname + ".trashinfo", "r")
print(a)

# Read the trashinfo file to get the original path of the file
for line in a:
    if "Path=" in line:  # Look for the line containing the original path of the file
        ab = re.findall(r'/.*', line)  # Extract the path using regex
        print(ab)

# Clean up the extracted path (remove extra characters)
destipath = str(ab)
destipath = destipath.lstrip('[')  # Remove the starting '[' character
destipath = destipath.rstrip(']')  # Remove the ending ']' character
destipath = destipath[:-1]  # Remove the last character (newline or other)
destipath = destipath[1:]  # Remove the first character (extra space)

print("Destination path is: " + destipath)

# Open the file in the Trash folder
file1 = open(path + "/" + fname, "r")
print(file1)

# Open the destination file where the recovered file will be stored
file2 = open(destipath, "w")
print(file2)

# Write the contents of the file from Trash to the destination
file2.write(file1.read())
file1.close()
file2.close()

print("File is recovered to destination")

# Remove the file from the Trash folder
os.remove(path + "/" + fname)
print("Removed from Trash: " + path + "/" + fname)

# Remove the corresponding .trashinfo file from the Trash info folder
os.remove(infopath + "/" + fname + ".trashinfo")
print("Removed from Trash info: " + infopath + "/" + fname + ".trashinfo")
