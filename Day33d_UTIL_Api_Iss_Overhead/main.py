# Day 33d Project
# IS ISS ABOVE YOU AND IS IT NIGHT
# Skills: API, API parameters, requests, smtplib, time.sleep, timer
# Notes:

import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.500000  # Your latitude - redacted
MY_LONG = -8.000000  # Your longitude - redacted

MY_EMAIL = "<Redacted>"
MY_PASSWORD = "<Redacted>"
SMTP_SERVER = "<Redacted>"
SMTP_PORT = 587
TARGET_EMAIL = "<Redacted>"


def is_iss_overhead():
    # Use API call to get ISS Latitude and Longitude coordinates
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        print("ISS is not overhead")
        return False


def is_it_dark():
    # Set parameters to pass into API Call
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # API Call to get current sunrise and sunset hour
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current hour from datetime.now()
    hour_now = datetime.now().hour

    # Check if it is nighttime (note this is over simplified to an hour level)
    if not sunrise_hour <= hour_now <= sunset_hour:
        return True
    else:
        print("It it not Dark")
        return False


def send_email_notification():
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=f"Subject:Look Up!!\n\nThe ISS is overhead")
        print(f"email sent to {TARGET_EMAIL}")


while True:
    print(f"{datetime.now().hour}:{datetime.now().minute}")

    # Note these function calls will return True / False so can resolve directly like this
    if is_iss_overhead() and is_it_dark():
        send_email_notification()

    time.sleep(60)
