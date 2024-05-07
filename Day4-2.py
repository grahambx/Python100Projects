# Udemy 100 Projects in 100 days
# Day 4 Learning
# NESTED LISTS
# Skills: Nested Lists
# Notes:

# Code to show set up and how to index a nested list


fruits = ["Orange", "Banana"]
vegetables = ["Potato", "Turnip"]
edibles = [fruits, vegetables]
print(edibles)            # [['Orange', 'Banana'], ['Potato', 'Turnip']]
print(edibles[1])         # ['Potato', 'Turnip']
print(edibles[1][1])      # Turnip
