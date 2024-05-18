# Udemy 100 Projects in 100 days
# Day 12 Project
# NUMBER GUESSING GAME
# Skills: Global Constants, Functions, Return
# Notes:

import random

# Global Constants
EASY_TURNS = 10
HARD_TURNS = 5


def difficulty():
    """Set difficulty and get number of turns a user has to guess number"""
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS


def check_answer(guess, answer, attempts):
    """Compare users guess against answer, decrease remaining attempts and return this"""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}.")


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = difficulty()
    answer = random.randint(1, 100)
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
