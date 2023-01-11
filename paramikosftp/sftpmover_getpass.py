#!/usr/bin/env python3
"""Lab 58.3 - Paramiko and SFTP"""
import paramiko #allows python to ssh
import os #low level operating system commands
import getpass #needed to accept passwords

def main():
    t = paramiko.Transport("10.10.2.3", 22) ##bender IP and port
    t.connect(username="bender", password=getpass.getpass()) 

    #make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    #copy firstpasswd.py script to bender container
    sftp.put("file_to_move.txt", "file_to_move.txt") #move file to target location home directory

    #close the connection
    sftp.close() 
if __name__ == "__main__":
    main()
