# Udemy 100 Projects in 100 days
# Day 4 Learning
# TREASURE MAP
# Skills: Nested Lists, Index Comparison, str.lower(), F String
# Notes:

# Program prints a 3x3 "Treasure Map".
# Can place an X on the map by defining input

coordinates = "B2"  # Change this A1 to C3
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = coordinates  # Where do you want to put the treasure?
letter = position[0].lower()  # force uniformity on casing
abc = ["a", "b", "c"]  # create a list index comparison
letter_index = abc.index(letter)  # this checks where the 'letter' sits in the abc list giving us the index
number_index = int(position[1]) - 1
treasure_map[number_index][letter_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
