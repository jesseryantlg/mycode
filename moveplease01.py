#!/usr/bin/env python3
"""A script to move two files into ceph_storage/"""

# standard library imports
import shutil #shell utilities will be used to move files
import os #provides access to low level os operations

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/') #move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/') #try moving the file into the ceph_storage directory

    #program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj?') #Collect string input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #moving kerrigan.obj to directory with new name

main() #this calls our main function

