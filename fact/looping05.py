#!/usr/bin/env python3
"""Looping across a file opened with 'with'
   wile also being gentle on memory consumption. 
   Sort domains ending in .org and .com into files org-domain.txt and com-domain.txt"""

#open file in read mode
with open("dnsservers.txt", "r") as dnsfile: #r is read mode

    #indent to keep the dns file open
    #loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') #remove newline character if it exists. It should exist on all but the last line. 
       

       #if the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile: #'a' is append mode
                srvfile.write(svr + "\n")
        #ELSE IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open ("com-domain.txt", "a") as srvfile: 
                srvfile.write(svr + "\n")

#file closes automatically

