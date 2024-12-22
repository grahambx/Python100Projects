# Udemy 100 Projects in 100 days
# Day 8 Project
# CAESAR CYPHER
# Skills: Functions, Parameters, Modulus, List, Index, While, For, If
# Notes:

# declare alphabet list variable
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# define character shifting function
# This will loop through each character in a string and offset it by the <shift_amount> in the direction based on <mode>
def caesar(mode, plain_text, shift_amount):
    new_text = ""
    if mode == "decode":
        shift_amount *= -1                              # If decoding we move in reverse so * -1
    for char in plain_text:
        if char not in alphabet:                        # If not in alphabet, keep unchanged
            new_text += char
        else:
            position = alphabet.index(char)             # Find char index
            position += shift_amount                    # shift the index by shift_amount
            new_text += alphabet[position]              # append the new_text with the character at the new index
    print(f"The {mode}d text is: {new_text}")


# Initiate user inputs and call caesar function
# program will repeat until user chooses to exit
end_program = False
while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26                                  # This accounts for only 26 chars in alphabet
    caesar(direction, text, shift)
    to_continue = input("\nType 'yes' to run again.\n")
    if to_continue != "yes":
        end_program = True
