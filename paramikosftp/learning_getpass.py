#!/usr/bin/env python3
"Lab 58.2 - Paramiko and SFTP | Jesse Ryan"""

#A simple python program to demonstrate getpass.getpass() to read passwords
import getpass

def main():
    p = getpass.getpass()
    print("Password entered:", p)

if __name__ == "__main__":
    main()

