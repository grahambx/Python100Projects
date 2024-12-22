# Udemy 100 Projects in 100 days
# Day 9 Project
# SECRET AUCTION
# Skills: Clear(), Dictionaries, For Loop, While Loop
# Notes:

from Day9_Art import logo

# create a function to allow clear() to clear the PyCharm Run window
# Believe this is pyCharm specific
# "Emulate terminal in output console" needs to be set for this specific .py file
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Loop to obtain user_names and bids, these are stored in a dictionary
more_bidders = True
bids = {}  # example: {"James": 125, "Chris": 325,}
while more_bidders:
    print(logo)
    print("Welcome to the secret auction program.")
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: £"))
    bids[user_name] = user_bid
    user_choice = input("Are there any other bidders? Type 'yes' or 'no': ")
    if user_choice == "yes":
        clear()
    else:
        more_bidders = False
        clear()


# Get bidder with highest bid
highest_bid = 0
winner = ""
for user in bids:
    if bids[user] > highest_bid:
        highest_bid = bids[user]
        winner = user

print(f"The winner is {winner} with a bid of £{highest_bid}")
