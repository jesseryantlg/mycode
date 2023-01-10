#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg #part 4 solution

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

     # SOLUTION TO PART 2
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    
    #Solution to Part 3
    #import datetime added above
    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    #return an ordered dictionary using lat/lon vars
    locator_resp= rg.search((lat, lon))

    #slice that object to return the city name only
    city = locator_resp[0]["name"]

    #slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    """)
    

if __name__ == "__main__":
    main()

