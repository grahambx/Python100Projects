# Day 32 Project
# SEND MOTIVATION EMAIL
# Skills: smtplib, email, datetime,
# Notes: See Python - smtplib page for email host setup etc

# If today is Thursday send a motivational email.

import smtplib
import datetime as dt
import random

MY_EMAIL = "Redacted and Revoked at Source"
MY_PASSWORD = "Redacted and Revoked at Source"
target_email = "Redacted and Revoked at Source"

now = dt.datetime.now()
day_of_week = now.weekday()  # 3 = today = Thursday

if day_of_week == 3:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        rand_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=target_email,
                            msg=f"Subject:Motivation\n\n{rand_quote}")
    print(rand_quote)

