#!/usr/bin/env python3
"""Using the CSV library to work with CSV Data | Jesse Ryan"""

#import csv library
import csv

#open csv data to loop across
with open("csv_users.txt", "r") as csvfile:
    #add a counter to create unique file names
    i = 0
    #loop across open files line by line
    for row in csv.reader(csvfile):
        i = i + 1 #increase by one to create unique file names
        filename = f"admin.rc{i}"  #this f string says" fill in the value of i"
        
        #open a file via "with". This file will autoclose when the indentations stop
        with open(filename, "w") as rcfile:
            #use the standard library print function to print our data to the open file "rcfile" in write mode
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" +row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" +row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

#when indentation ends, all files are autoclosed
#display this to the screen with the looping is over
print("admin.rc files created!")

