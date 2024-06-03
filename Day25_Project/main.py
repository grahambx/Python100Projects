# Udemy 100 Projects in 100 days
# Day 25 Project
# GUESS THE STATE GAME
# Skills: Pandas, Csv, Turtle, Screen, Images, Iloc, List Comprehension
# Notes: Added List Comprehension in lesson 26

import turtle
import pandas
from PIL import Image

# Note, I had an issue whereby the image was not fixed to screen
# I had to change screen.addshape(image) to turtle.bgpic(image)
# and use img.size code below to match the screen size
img = Image.open("blank_states_img.gif")
width, height = img.size

screen = turtle.Screen()
screen.title("Name the states")
screen.setup(width=width, height=height)

image = "blank_states_img.gif"
turtle.bgpic(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()     # strip the states column to a list to making checking easier later


game_is_on = True
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        not_guessed = [state for state in all_states if state not in correct_guesses]
        # above line using list comprehension replaces the 4 below
        # not_guessed = []
        # for state in all_states:
        #     if state not in correct_guesses:
        #         not_guessed.append(state)
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        # Note below was course approach but got warning using int() in this fashion is deprecated.
        # the above is the now preferred integer location attribute
        # t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guesses.append(answer_state)

screen.exitonclick()
