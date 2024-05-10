# Udemy 100 Projects in 100 days
# Day 3 Learning
# ROLLERCOASTER PRICE CALCULATOR
# Skills: If Elif Else,
# Notes:

# This code asks for a customers height to see if they are tall enough for the Roller Coaster
# If they are above 120cm we then confirm age which define the ticket cost
# We also ask if the customer would like a photo and add this to the price

# Get Customer Height
print("Welcome to rollercoaster")
height = int(input("What is your height in cm? \n"))

if height > 120:
    print("you can ride")
    # Get Customer Age and Calculate base price to ride
    age = int(input("What is your age? \n"))
    if age <= 12:
        base_cost = 50
    elif age > 12 and age <= 18:
        base_cost = 40
    elif age >= 45 and age <= 55:
        base_cost = 0
        print("You get to ride for free!!")
    else:
        base_cost = 30
    # Get Customer Photo Requirement and increment price if needed
    photos = input("Do you want photos? (Y/N): \n")
    if photos.upper() == "Y":
        base_cost += 3
    print(f"Total cost is {base_cost}")
else:
    print("No chance kid")
