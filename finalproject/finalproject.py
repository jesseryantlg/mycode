#!/usr/bin/env python3
"""Final Project - Topic TBD | Jesse Ryan"""
import requests

censusAPI= "https://api.census.gov/data/2021/acs/acs1/pums?get=PWGTP,AGEPs"
age_date = requests.get("f{censusAPI}[0][1]")
print(age_date)

#import requests

#censusAPI = "https://api.census.gov/data/2021/acs/acs1/pums"

#def main():
 #   age_data = requests.get(f"{censusAPI}PWGTP,AGEP")

  #  print( age_data.json().keys() )

#if __name__ == "__main__":
 #   main()
