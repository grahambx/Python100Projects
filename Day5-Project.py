# Udemy 100 Projects in 100 days
# Day 5 Project
# PASSWORD GENERATOR
# Skills: Lists, Random, For Loop, Range, Shuffle
# Notes: See end of code for complex solution to shuffle a list without using the shuffle method

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# get user provided password parameters
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create one list with the correct amount of each character type as specified by user
# First create empty list - then use for loops to append randomly selected characters as needed

char_list = []
for char in range(1, nr_letters+1):
    char_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    char_list.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    char_list.append(random.choice(numbers))
print(char_list)

# Now we need to randomise the order
# Simpler approach is to use the random.shuffle method
# This shuffles a list in place

random.shuffle(char_list)
print(char_list)

# Will leave 2 existing print statements to demonstrate randomisation
# However need to print password as a string

password = ""
for char in char_list:
    password += char
print(f"\nYour password is: {password}")

# END

# Note below is my first attempt at randomisinf the order of the char_list
# It works but is overly complex compared to the shuffle method

# We will use random.choice() method to pick a random character from char_list then place in new password list object
# We need to clear down 'selected' characters from char_list to prevent duplication
'''
password = []
for chars in range(1, len(char_list)+1):
    char = random.choice(char_list)
    password.append(char)
    char_list.remove(char)
print(password)
'''