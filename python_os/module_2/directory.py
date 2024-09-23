import os

# Get current directory
print(os.getcwd())

# # Make new directory
os.mkdir("new_dir")

# # Change directory
os.chdir("new_dir")

# # Remove directory
os.rmdir("new_dir")

# Get list of all files and sub directory
print(os.listdir(os.getcwd()))

# Check if is adirectory
os.path.isdir("path")

# Check if a file
os.path.isfile("file")

