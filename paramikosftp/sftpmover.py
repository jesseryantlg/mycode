#!/usr/bin/env python3
""" Lab 58 - Paramiko and SFTP | Jesse Ryan"""

##import paramiko to talk SSH
import paramiko
import os

##define the connection location
t = paramiko.Transport("10.10.2.3",22) #IP and Port#

#define how to connect
t.connect(username="bender", password="alta3")

#define an sftp object
sftp = paramiko.SFTPClient.from_transport(t)

#iterate across files in the directory
for x in os.listdir("/home/student/filestocopy/"): 
    if not os.path.isdir("/home/student/filestocopy/"+x): #filter everything that is not a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) #move file to target location

##close the connections
sftp.close()
t.close()

