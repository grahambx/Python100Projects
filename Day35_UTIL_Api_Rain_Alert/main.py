# Day 35 Project
# RAIN ALERT
# Skills: API, secrets, dotenv, env variables, whatsapp
# Notes: Day17 > Day34

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Use dotenv approach to store keys etc
load_dotenv()

# Note OMW api will return the weather forecast every 3 hours for the next 5 days
# API documentation: https://openweathermap.org/forecast5
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
OWM_api_key = os.getenv("OWM_api_key")

# Note twilio API used for sending Whatsapp messages
# API documentation: https://www.twilio.com/docs/whatsapp/api
twilio_account_sid = os.getenv("twilio_account_sid")
twilio_auth_token = os.getenv("twilio_auth_token")
twilio_whatsapp_number = os.getenv("twilio_whatsapp_number")
twilio_target_number = os.getenv("twilio_target_number")

# OWM API Call
parameters = {
    "lat": 51.524735,
    "lon": -3.103480,
    "appid": OWM_api_key,
    "cnt": 4,              # This restricts response to next 4 records only (12 hours)
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

# Can use this data to determine if it will rain in next 12 hours.
# Note the "cnt" parameter restricts to next 4x3 hours
# the JSON has a list object with data for each day, some nesting
# Any id < 700 is some sort of rain or snow
will_rain = False
for _ in data["list"]:
    if _["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    # twilio API call
    # This sends a whatsapp
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        from_=f"whatsapp:{twilio_whatsapp_number}",
        body="It's going to rain today. Bring a Brolly!",
        to=f"whatsapp:{twilio_target_number}"
    )
    print(message.status)
else:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages.create(
        from_=f"whatsapp:{twilio_whatsapp_number}",
        body="No rain today. Take sunnies!",
        to=f"whatsapp:{twilio_target_number}"
    )
    print(message.status)

# below not part of lesson, but this was me learning JSON and having fun
for _ in data["list"]:
    dt_txt = _["dt_txt"]
    weather = _["weather"][0]["main"]
    description = _["weather"][0]["description"]
    temp = _["main"]["temp"]
    temp_c = int(temp - 273.15)
    weather_type_id = _["weather"][0]["id"]
    print(f"{dt_txt} - {temp_c} - {weather_type_id} - {weather} - {description}")
