# Udemy 100 Projects in 100 days
# Day 13 Project
# HIGHER OR LOWER GAME
# Skills: Functions, Modules, Dictionary, List, Random,
# Notes: Worked as excepted and much closer to lesson output approach. Asking Co-pilot to compare the code it suggests i
# could improve: Make function names more descriptive, Make functions have a single clear purpose and
# don't nest functions like I did with make unique.

import random
from Day13_Data import data


# Get 2 initial choices from data, make sure they are different with make_unique()
def get_choices():
    choice_a = random.choice(data)
    choice_b = random.choice(data)
    make_unique(choice_a, choice_b)
    return choice_a, choice_b


# Ensure the 2 choices are unique
def make_unique(choice_a, choice_b):
    while choice_a == choice_b:
        choice_b = random.choice(data)


# If a player was right retain the correct choice and get a new one. Retained task must move to choice_a
def update_choices(choice_a, choice_b, decision):
    if decision == "b":
        choice_a = choice_b
    choice_b = random.choice(data)
    make_unique(choice_a, choice_b)
    return choice_a, choice_b


# Shows choices to user and prompts for higher lower decision
def get_input(choice_a, choice_b):
    print(f"Compare A: {choice_a["name"]}, a {choice_a["description"]}, from {choice_a["country"]}.")
    print(f"Against B: {choice_b["name"]}, a {choice_b["description"]}, from {choice_b["country"]}.")
    return input("Who has more followers? Type 'A' or 'B': ")


# Check if user was correct
def get_result(choice_a, choice_b, decision):
    """checks is user was correct, if they are load in a new choice for next round"""
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return decision == 'a'
    else:
        return decision == 'b'


def game():
    # set base game parameters and use function to set the 2 choices user will see
    score = 0
    choice_a, choice_b = get_choices()
    # call function to display choices to user and prompt for a decision on if A or B is higher
    decision = get_input(choice_a, choice_b).lower()
    # as long as player keeps getting it right the game continues
    while get_result(choice_a, choice_b, decision):
        score += 1
        print(f"\nYou're right! Current Score: {score}")
        # function needed which keeps the correct choice and gets a new one
        choice_a, choice_b = update_choices(choice_a, choice_b, decision)
        # prompt the user for new decision
        decision = get_input(choice_a, choice_b).lower()
    # final output when player loses
    print(f"Sorry, that's wrong. Final score: {score}")
    print(f"{choice_a["name"]} has {choice_a["follower_count"]}m followers")
    print(f"{choice_b["name"]} has {choice_b["follower_count"]}m followers")


game()
