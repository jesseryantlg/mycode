#!/usr/bin/env python3
"""NASA APIs | Jesse Ryan"""

import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ##Define credentials
    with open("/home/student/mycode/nasaapi/nasa.creds") as mycreds:
        nasacreds = mycreds.read()
        
    ##remove extra characters from the mycreds.read() key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ##Call the webservice with the key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)
    
    #read the file like object
    apodread = apodurlobj.read()

    ##decode JSON to Python data structure
    apod = json.loads(apodread.decode("utf-8"))

    ##display data in Python format
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"] + "\n")
    print(apod["url"])

if __name__ == "__main__":
    main()
