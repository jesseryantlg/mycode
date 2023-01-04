#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") #prompts user for input

#if user set IP of gateway
if ipchk == "192.168.70.1":
    print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: #if any data is provided, this will test if true
    print("Looks like the IP address was set: " + ipchk) #indented under if
else: #if nothing provided
    print("You did not provide input.")
