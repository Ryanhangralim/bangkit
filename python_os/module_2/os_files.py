import os

# Check if file exist
print(os.path.exists("test_write.txt"))

# # Rename
os.rename("test.txt", "new_renamed_test.txt")

# # Remove
os.remove("new_renamed_test.txt")

# Get file size
print(os.path.getsize("example_file.txt"))

# get mtime
print(os.path.getmtime("example_file.txt"))

# Get better format
import datetime
timestamp = os.path.getmtime("example_file.txt")
print(datetime.datetime.fromtimestamp(timestamp))

# Convert to absolute path
print(os.path.abspath("example_file.txt"))