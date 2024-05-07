# Udemy 100 Projects in 100 days
# Day 4 Project
# ROCK SCISSORS PAPER GAME
# Skills: Lists, Nested Lists, Module Import, Random
# Notes: Course Answer was a long list of elifs instead of a outcome matrix

# Simple Rock Scissors Paper Game

import random

# Define a list of Rock Scissor Paper Asci Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock, paper, scissors]

# Obtain and display user choice
user_choice = int(input("What do you Choose?\nType 1 for Rock\nType 2 for Paper\nType 3 for Scissors\n"))
user_choice = user_choice - 1
print(f"You chose:\n{choice[user_choice]}")

# Obtain and display randomised computer choice
program_choice = random.randint(0, 2)
print(f"Computer chooses:\n{choice[program_choice]}")

# Define a 3x3 outcome list matrix
user_Rock = ["It's a Draw", "You Loose", "You Win"]
user_Paper = ["You Win", "It's a Draw", "You Loose"]
user_scissors = ["You Loose", "You Win", "You Loose"]
outcome_matrix = [user_Rock, user_Paper, user_scissors]

# Print Outcome
print(outcome_matrix[user_choice][program_choice])
