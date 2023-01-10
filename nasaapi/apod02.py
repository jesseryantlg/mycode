#!/usr/bin/env python3
"""NASA API 2 | Jesse Ryan"""

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ##retrieve credentials
    with open("/home/student/mycode/nasaapi/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    #remove newline characters from api key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

def main():
    #grab credentials
    nasacreds = returncreds()
    
    #Call NASA API with our key
    apodresp = requests.get(NASAAPI + nasacreds)
    
    #strip off JSON
    apod = apodresp.json()

    print(apod)
    print()
    print(apod["title"] + "\n")
    print(apod["date"] + "\n")
    print(apod["explanation"] + "\n")
    print(apod["url"])

if __name__ == "__main__":
    main()


