# Udemy 100 Projects in 100 days
# Day 24 Project
# MAIL MERGE
# Skills: Files, Read, Write, Create, Directories
# Notes:


with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()  # this captures each line as a string item in a list

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # this has copied the template letter as 1 string object
    for name in names:
        stripped_name = name.strip()  # this removes the '\n' that was added to the end of each item in the names list
        new_letter = letter_contents.replace("[name]", stripped_name)  # makes new letter and updates the name
        # then for each name in names we use open with mode= w to effectively create a new file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as output_file:
            output_file.write(new_letter)

