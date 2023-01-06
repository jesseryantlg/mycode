#!/usr/bin/env python3
"""Lab 47 Customization 1 | Jesse Ryan"""

loginfail =  0
loginget = 0
loginpost = 0 
failips = []
with open("keystone.common.wsgi", "r") as faillog:
    for line in faillog:
        if "GET" in line:
            loginget += 1
        if "POST" in line:
            loginpost += 1
        if "Authorization failed" in line:
            loginfail += 1
            ip = line.split()[-1]
            failips.append(ip)
            with open("errors.txt", "a") as errorfile:
                    errorfile.write(line + "\n")

print("The number of failed attempts is:", loginfail)
print("The number of POSTS is:", loginpost)
print("The number of GETS is:", loginget)


