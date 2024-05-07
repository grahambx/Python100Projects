# Udemy 100 Projects in 100 days
# Day 3 Project
# TEXT ADVENTURE GAME
# Skills: If Elif Else, str.lower()
# Notes:

# Simple text adventure game with 3 decision/inflection points
# ASCI art from ascii.co.uk/art

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|________
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
# Get User Decision 1
direction = input("Welcome to Treasure Island.   You come to a fork in the road, do you go right or left? ")
direction = direction.lower()
if direction == "right":
    print("You fell into a trap pit, GAME OVER")
else:
    # Get User Decision 2
    swimwait = input('A bear starts chasing you, you run out of road and come to a river, do you "Swim" or "Wait"?')
    swimwait = swimwait.lower()
    if swimwait == "swim":
        print("You get eaten by a fish. GAME OVER")
    else:
        # Get User Decision 3
        side = input('He\'s a friendly bear, awwww!! He flips a coin, do you choose "Heads", "Tails" or anything else?')
        side = side.lower()
        if side == "heads":
            print("He wasn't friendly... He bites off your head. \nGAME OVER")
        elif side == "tails":
            print("You pull his tail which sets off some celebratory fireworks. \n WINNER WINNER CHICKEN DINNER")
        else:
            print(f'The bear scowls at you "What sort of answer is.... {side}" he yells before mauling you\nYou Loose')
