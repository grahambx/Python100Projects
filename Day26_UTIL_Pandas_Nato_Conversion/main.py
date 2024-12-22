# Udemy 100 Projects in 100 days
# Day 26 Project
# NATO ALPHABET CONVERSION
# Skills: Pandas, Dataframes, List Comprehension, Dictionary Comprehension
# Notes:

import pandas
# quick and easy to pull into a dataframe
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# however a dict will make it easier to pull out values for keys
# below we use dictionary comprehension to construct this
nato = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Name please?:").upper()
# our output is just a list of the nato codes, so using list comprehension to construct this
output_list = [nato[char] for char in name]
print(output_list)
