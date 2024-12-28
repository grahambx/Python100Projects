# Day 33c Project
# GET SUNRISE AND SUNSET DETAILS
# Skills: API, API parameters, requests, non-standard dates, datetime
# Notes:

import requests
from datetime import datetime

USER_POSITION = (51.519124, -3.093174)

latitude = USER_POSITION[0]
longitude = USER_POSITION[1]

# See [[Python - APIs]] for more detail, including how you could manipulate the API call string as well to pass
# these parameters. However this approach is cleaner
parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0,  # This is optional, but default is "1" which returns in a 12 hour format, not desired this work
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# The API returns the time in a non-standard string format, here we manipulate the string to pull out the hour
# Splitting on T gives date in index[0] and time in index[1]
# So Take index[1] and split on : Now index[0] from this output is the hour
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

now = datetime.now()

print(sunrise)
print(now.hour)
