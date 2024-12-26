# Day 32 Project
# SEND BIRTHDAY EMAILS
# Skills: smtplib, email, datetime, pandas, webhosting
# Notes: See "Python - smtplib" page for email host setup etc, see "Python - Host" for how to host/schedule code on web

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "learninggraham@gmail.com"
MY_PASSWORD = "nddj xojw bjti xawc"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Get current month and date
now = dt.datetime.now()
month = now.month
day = now.day

# read in birthdays.csv as DataFrame
data = pandas.read_csv("birthdays.csv")

# loop through the DataFrame to find any records that match today's day and month
for (index, row) in data.iterrows():
    if row.month == month and row.day == day:
        # When you get a match, pull out required data points, choose and update a random letter, then send email
        name = row["name"]
        email = row["email"]
        letter = random.choice(letters)
        with open(f"./letters/{letter}") as rand_letter:
            orig_contents = rand_letter.read()
            new_contents = orig_contents.replace("[NAME]", str(name))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!!\n\n{new_contents}")
            print(f"email sent to {email}")

