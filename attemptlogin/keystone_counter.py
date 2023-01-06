#!/usr/bin/env python3
"""Parsing log files | Jesse Ryan"""

loginfail = 0 #starting a counter for failed login attempts

#open log file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") 

#turn the file into a list of lines in memory
keystone_file_lines= keystone_file.readlines()

#loop over the list of lines
for line in keystone_file_lines:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 #this is the same as loginfail = loginfail + 1
print("The number of failed login attempts is", loginfail)
keystone_file.close() #close the open file
