#!/usr/bin/env python3
"""Catching specific errors | Jesse Ryan """

#start with an infinite loop
while True: 
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    #general error ahndling
    #a practical use might be exceptions we haven't designed solutions for yet.
    except Exception as err:
        #sys.exc_info returns a 3 tuple with info about the excption handled
        print("We did not anticipate that:",err)

