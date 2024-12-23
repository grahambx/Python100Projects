# Udemy 100 Projects in 100 days
# Day 30 Project
# NATO ALPHABET CONVERSION + EXCEPTIONS
# Skills: Pandas, Dataframes, List Comprehension, Dictionary Comprehension, Exceptions
# Notes: Build on Day26 Project

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_nato():
    name = input("Name please?:").upper()
    try:
        output_list = [nato[char] for char in name]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_nato()
    else:
        print(output_list)


generate_nato()
