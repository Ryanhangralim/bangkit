### BASIC LINUX COMMANDS
mkdir mynewdir
cd mynewdir/
/mynewdir$ pwd
/mynewdir$ cp ../spider.txt .
/mynewdir$ touch myfile.txt
/mynewdir$ ls -l 
#Output:
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 myfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
/mynewdir$ ls -la
#Output:
#total 12
#drwxr-xr-x  2 user user  4096 Mai 22 14:17 .
#drwxr-xr-x 56 user user 12288 Mai 22 14:17 ..
#-rw-rw-r--  1 user user     0 Mai 22 14:22 myfile.txt
#-rw-rw-r--  1 user user   192 Mai 22 14:18 spider.txt
/mynewdir$ mv myfile.txt emptyfile.txt
/mynewdir$ cp spider.txt yetanotherfile.txt
/mynewdir$ ls -l
#Output:
#total 8
#-rw-rw-r-- 1 user user   0 Mai 22 14:22 emptyfile.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:18 spider.txt
#-rw-rw-r-- 1 user user 192 Mai 22 14:23 yetanotherfile.txt
/mynewdir$ rm *
/mynewdir$ ls -l
#total 0
/mynewdir$ cd ..
rmdir mynewdir/
ls mynewdir
#ls: cannot access 'mynewdir': No such file or directory

### REDIRECTING STREAMS

#Output: Don't mind me, just a bit of text here...
./stdout_example.py > new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
./stdout_example.py >> new_file.txt
cat new_file.txt 
#Output: Don't mind me, just a bit of text here...
 #Don't mind me, just a bit of text here...
cat streams_err.py 
#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
./streams_err.py < new_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
./streams_err.py < new_file.txt 2> error_file.txt
#This will come from STDIN: Now we write it to STDOUT: Don't mind #me, just a bit of text here...
cat error_file.txt 
#Traceback (most recent call last):
  #File "./streams_err.py", line 5, in <module>
    #raise ValueError("Now we generate an error to STDERR")
#ValueError: Now we generate an error to STDERR
echo "These are the contents of the file" > myamazingfile.txt
cat myamazingfile.txt 
#These are the contents of the file


### PIPES AND PIPELINES
ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
     # 7 the
     # 3 up
     # 3 spider
     # 3 and
     # 2 rain
     # 2 itsy
     # 2 climbed
     # 2 came
     # 2 bitsy
     # 1 waterspout.

cat capitalize.py
#!/usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip().capitalize())

cat haiku.txt 
#advance your career,
#automating with Python,
#it's so fun to learn.

cat haiku.txt | ./capitalize.py 
#Advance your career,
#Automating with python,
#It's so fun to learn.

./capitalize.py < haiku.txt
#Advance your career,
#Automating with python,
#It's so fun to learn.

### SIGNALING PROCESSES
ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes

ping www.example.com
#PING www.example.com(2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946)) 56 data bytes
# ctrl + z : stops the command, fg continues it
fg
#ping www.example.com
#64 bytes from 2606:2800:220:1:248:1893:25c8:1946 (2606:2800:220:1:248:1893:25c8:1946): icmp_seq=5 ttl=51 time=93.6 ms

# SUMMARY
Managing streams
These are the redirectors that we can use to take control of the streams of our programs

command > file: redirects standard output, overwrites file

command >> file: redirects standard output, appends to file

command < file: redirects standard input from file

command 2> file: redirects standard error to file

command1 | command2: connects the output of command1 to the input of command2

Operating with processes
These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

ps: lists the processes executing in the current terminal for the current user

ps ax: lists all processes currently executing for all users  

ps e: shows the environment for the processes listed  

kill PID: sends the SIGTERM signal to the process identified by PID

fg: causes a job that was stopped or in the background to return to the foreground

bg: causes a job that was stopped to go to the background

jobs: lists the jobs currently running or stopped

top: shows the processes currently using the most CPU time (press "q" to quit

### CREATING BASH SCRIPTS
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"

##OUTPUT
Starting at: Mi 22. Mai 17:13:06 CEST 2019

UPTIME

 17:13:06 up 8 days,  1:34,  2 users,  load average: 0,00, 0,00, 0,00

FREE

              total        used        free      shared  buff/cache   available

Mem:        4037132      871336      253940       10032     2911856     2865984

Swap:       2097148        4364     2092784

WHO

user     :0           2019-05-14 15:39 (:0)

user     pts/1        2019-05-14 15:40 (192.168.122.1)

Finishing at: Mi 22. Mai 17:13:06 CEST 2019

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"

## OUTPUT

Starting at: Mon 13 May 2019 02:52:11 PM CEST

UPTIME

 14:52:11 up 17 days,  2:35,  1 user,  load average: 0.70, 1.01, 1.16

FREE

              total        used        free      shared  buff/cache   available

Mem:       32912600    19966400     1003304      321672    11942896    12281516

Swap:      20250620      612352    19638268

WHO

user    tty7         2019-04-29 12:19 (:0)

Finishing at: Mon 13 May 2019 02:52:11 PM CEST

### USING VARIABLES AND GLOBS
line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

## OUTPUT
Starting at: Mi 22. Mai 17:30:30 CEST 2019

-------------------------------------------------

UPTIME

 17:30:30 up 8 days,  1:51,  2 users,  load average: 0,00, 0,00, 0,00

-------------------------------------------------

FREE

              total        used        free      shared  buff/cache   available

Mem:        4037132      862132      444720       10032     2730280     2875336

Swap:       2097148        6156     2090992

-------------------------------------------------

WHO

user     :0           2019-05-14 15:39 (:0)

user     pts/1        2019-05-14 15:40 (192.168.122.1)

-------------------------------------------------

Finishing at: Mi 22. Mai 17:30:30 CEST 2019


### CONDITIONAL EXECUTION IN BASH
if grep "127\.0\.0\.1" /etc/hosts; then

	echo "Everything ok"

else

	echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi 

## OUTPUT
127.0.0.1	localhost

Everything ok

if test -n "$PATH"; then echo "Your path is not empty"; fi

## output
Your path is not empty


if [ -n "$PATH" ]; then echo "Your path is not empty"; fi

## output
Your path is not empty

# ADVANCED BASH CONCEPTS
n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done

## output
Iteration number 1

Iteration number 2

Iteration number 3

Iteration number 4

Iteration number 5


import random

value=random.randint(0, 3)

print("Returning: " + str(value))

sys.exit(value)

## output

Returning: 3

Returning: 2

Returning: 0

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
        sleep $n
        ((n+=1))
        echo "Retry #$n"
done;


## output ./retry.sh ./random-exit.py
Returning: 3

Retry #1

Returning: 3

Retry #2

Returning: 1

Retry #3

Returning: 3

Retry #4

Returning: 0

### FOR LOOPS IN BASH
for fruit in peach orange pear; do

        echo "I like $fruit!"

Code output:

I like peach!

I like orange!

I like pear!


cd old_website/
/old_website$ ls -l

  Code output:

total 0

-rw-r--r-- 1 user user 0 May 24 10:19 about.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 contact.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 footer.HTM

-rw-r--r-- 1 user user 0 May 24 10:20 header.HTM

-rw-r--r-- 1 user user 0 May 24 10:19 index.HTM

/old_website$ basename index.HTM .HTM # This command takes a filename and an extension, and then returns the name without the extension.


for file in *.HTM; do
        name=$(basename "$file" .HTM)
        echo mv "$file" "$name.html" 
done

# The script iterates through all files with the ".HTM" extension in the current directory. For each file, it extracts the filename without the extension and generates the new filename with the ".html" extension. Finally, it prints the mv command that would rename the original file to the new filename.

# Note: This script only prints the mv commands. To actually rename the files, you need to execute the script by running chmod +x script.sh && ./script.sh where script.sh is the name of the script file.



/old_website$ chmod +x rename.sh
/old_website$ ./rename.sh 

About this code
Here the script gets saved as rename.sh

Code output:

mv about.HTM about.html

mv contact.HTM contact.html

mv footer.HTM footer.html

mv header.HTM header.html

mv index.HTM index.html


/old_website$ ./rename.sh 
/old_website$
/old_website$ ls -l

About this code
These commands won’t print anything. That's expected because these commands don't print anything when they succeed.

ls -l 

About this code
ls -l is a command in Linux and Unix systems used to list the contents of a directory in a long format. This format provides detailed information about each file

Code output:

total 4

-rw-r--r-- 1 user user  0 May 24 10:19 about.html

-rw-r--r-- 1 user user  0 May 24 10:20 contact.html

-rw-r--r-- 1 user user  0 May 24 10:20 footer.html

-rw-r--r-- 1 user user  0 May 24 10:20 header.html

-rw-r--r-- 1 user user  0 May 24 10:19 index.html

-rwxr-xr-x 1 user user 90 May 24 10:40 rename.sh


## ADVANCED COMMAND INTERACTION
tail /var/log/syslog

Code output:

May 24 10:17:01 ubuntu.local CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

May 24 10:18:41 ubuntu.local rsyslogd: -- MARK --

May 24 10:25:19 ubuntu.local systemd[1]: Reloading.


tail /var/log/syslog | cut -d' ' -f5-

Code output:

CRON[257236]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)

rsyslogd: -- MARK --

systemd[1]: Reloading.


cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head

  Code output:

     41 systemd[1]: Starting Network Manager Script Dispatcher Service...

     41 systemd[1]: Started Network Manager Script Dispatcher Service.

     41 systemd[1]: NetworkManager-dispatcher.service: Succeeded.

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: start running ordered scripts...

     41 nm-dispatcher: req:1 'dhcp4-change' [ens3]: new request (1 scripts)

     41 dhclient[757]: DHCPREQUEST for 192.168.122.103 on ens3 to 192.168.122.1 port 67 (xid=0x3a5ff7ed)

     41 dhclient[757]: DHCPACK of 192.168.122.103 from 192.168.122.1 (xid=0xedf75f3a)

     41 dbus-daemon[592]: [system] Successfully activated service 'org.freedesktop.nm_dispatcher'

     41 dbus-daemon[592]: [system] Activating via systemd: service name='org.freedesktop.nm_dispatcher' unit='dbus-org.freedesktop.nm-dispatcher.service' requested by ':1.15' (uid=0 pid=599 comm="/usr/sbin/NetworkManager --no-daemon " label="unconfined")

      9 systemd[1]: Started Run anacron jobs.

#!/bin/bash

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done

About this code
This script is written in the Bash scripting language and designed to analyze log files. It analyzes each log file in the /var/log directory and displays the top 5 most frequently occurring messages along with their counts.

./toploglines.sh

Code output:

(...)

Processing: /var/log/user.log

     23 system-updater[199481]: DEBUG Command exited with status: 0

     19 system-updater[46682]: DEBUG Command exited with status: 0

     16 system-updater[175060]: DEBUG Command exited with status: 0

     11 /usr/bin/lock: called by /bin/bash for . uid 0, euid 0.

     11 network-manager-dhclient-hooks: Dispatching run of '/etc/dhcp/dhclient-exit-hooks.d/hostname' ...

Processing: /var/log/Xorg.0.log

     87 Printing DDC gathered Modelines:

     87 Modeline "1920x1080"x0.0  141.00  1920 1936 1952 2104  1080 1083 1097 1116 -hsync -vsync (67.0 kHz eP)

     87 EDID vendor "AUO", prod id 5949

     78 vendor "AUO", prod id 5949

     78 DDC gathered Modelines:

# CHOSING BETWEEN BASH AND PYTHON

for i in $(cat story.txt); do B=`echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"`; echo -n "${B}${i:1} "; done; echo -e "\n"

About this code
This code snippet is written in the Bash scripting language and designed to capitalize the first letter of each word in a text file. This script iterates through each line in the story.txt file and capitalizes the first letter of each word. It then prints the modified text to the output.


import sys

for line in sys.stdin:

    words = line.strip().split()

    print(" ".join([word.capitalize() for word in words]))

About this code
This script takes input from a text file  or from another command, removes the whitespace, splits it into separate words, capitalizes the first letter of each word in every line, and prints the modified text to the standard output. 


cat story.txt | ./capitalize_words.py 

Code output:

Once Upon A Time There Was An Egg Of A Programming Language Called Python~