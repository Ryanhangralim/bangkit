import os
import sys 
import subprocess
import re

# def to_seconds(hours, minutes, seconds):
#     return hours*3600+minutes*60+seconds

# print("Welcome to this time converter")

# cont = "y"
# while(cont.lower() == "y"):
#     hours = int(input("Enter the number of hours: "))
#     minutes = int(input("Enter the number of minutes: "))
#     seconds = int(input("Enter the number of seconds: "))

#     print("That's {} seconds".format(to_seconds(hours, minutes, seconds)))
#     print()
#     cont = input("Do you want to do another conversion? [y to continue] ")
    
# print("Goodbye!")

# Get environment variables
# Set env variable = set VARIABLE_NAME=Value
# print("Fruit: " + os.environ.get("FRUIT"))

# Command line arguments
# print(sys.argv)
# sys.exit(1)

# Subprocess
# subprocess.run(["date"])
# subprocess.run(["sleep" ,"2"])
# result = subprocess.run(["ls", "this_file_does_not_exist"])
# print(result)

# result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# print(result.returncode)
# print(result.stdout)
# print(result.stdout.decode().split())

# result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
# print(result.returncode)
# print(result.stdout)
# print(result.stderr)

# my_env = os.environ.copy()
# my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# result = subprocess.run(["myapp"], env=my_env)

"""
Subprocesses are a way to call and run other applications from within Python, including other Python scripts.
In Python, the subprocess module can run new codes and applications by launching the new processes from the Python program. Because subprocess allows you to spawn new processes, it is a very useful way to run multiple processes in parallel instead of sequentially.

Python subprocess can launch processes to: 

Open multiple data files in a folder simultaneously. 

Run external programs. 

Connect to input, output, and error pipes and get return codes.

Subprocess is best used when you need to interface with external processes, run complex shell commands, or need precise control over input and output. Subprocess also spawns fewer processes per task than OS, so subprocess can use less compute power. 
On the other hand, OS is useful for basic file and directory operations, environment variable management, and when you don't need the object-oriented approach provided by Pathlib. 
Finally, Pathlib is most helpful for working extensively with file paths, when you want an object-oriented and intuitive way to handle file system tasks, or when you're working on code where readability and maintainability are crucial. 
"""

# Filtering log files with regular expression
# logfile = sys.argv[1]
# usernames = {}
# with open(logfile) as f:
#   for line in f:
#     if "CRON" not in line:
#       continue
#     pattern = r"USER \((.+)\)$"
#     result = re.search(pattern, line)
#     if result is None:
#       continue
#     name = result[1]
#     usernames[name] = usernames.get(name, 0) + 1

# def show_time_of_pid(line):
#   pattern = r"(Jul \d+ \d+:\d+:\d+).*?\[(\d+)\]"
#   result = re.search(pattern, line)
#   return result.group(1) + " pid:" + result.group(2)

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
