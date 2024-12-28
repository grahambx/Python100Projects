# Day 33a Project
# GET ISS POSITION
# Skills: API, requests
# Notes:

import requests

# make api call
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()  # use the built-in exception handling

# pull out the json response data
data = response.json()

# extract required fields from the json to variables
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# combine the lat/long for printing
iss_position = (longitude, latitude)

print(iss_position)
