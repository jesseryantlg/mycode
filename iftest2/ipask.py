#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") #this line prompts a user for input

#a provided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk) #indented under if
else: #if no data is provided
    print("You did not provide input.") #indented under else

