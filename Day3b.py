# Udemy 100 Projects in 100 days
# Day 3 Lesson Workings
# RollerCoaster cost calculator
# if elif else

print("Welcome to rollercoaster")
height = int(input("What is your height in cm? \n"))

if height > 120:
    print("you can ride")
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
    photos = input("Do you want photos? (Y/N): \n")
    if photos.upper() == "Y":
        base_cost += 3
    print(f"Total cost is {base_cost}")
else:
    print("No chance kid")
