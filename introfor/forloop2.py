#!/usr/bin/env python3
"""For Loops 2 | Jesse Ryan"""

#create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta", "zach", "stuart"]

#create a second list of strings

approved_vendors = ["cisco", "juniper", "big_ip"]

#loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="") #new line, print current vendor, and end without a new line
    if x not in approved_vendors:  #if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
    print("\nOur loop has ended.") #print when loop finished
