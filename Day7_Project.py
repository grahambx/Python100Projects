# Udemy 100 Projects in 100 days
# Day 7 Project
# HANGMAN GAME
# Skills: Modules, Import, Random.Choice, For, While
# Notes: Support modules for Art and Word List

import random
from Day7_Art import stages, logo
from Day7_Words import word_list

# Choose a random word from the word list and get its length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initiate game condition variables
end_of_game = False
lives = 6

# print logo
print(logo)

# Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Create blank string matching length of chosen word
display = []
for _ in range(word_length):
    display += "_"

# Start main game loop, will run until end_of_game = True
while not end_of_game:
    # Get user guess
    guess = input("Guess a letter: ").lower()

    # Advise user if repeat guess
    if guess in display:
        print(f"You have already guessed {guess}, please try another")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position} -- Current letter: {letter} -- Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # If guess is wrong, decrease lives and check end_of_game status
    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry {guess} is not in the word. You have {lives} lives remaining!")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")  # join method returns iterables of a list as 1 string with a seperator

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print Stage Graphic
    print(stages[lives])
