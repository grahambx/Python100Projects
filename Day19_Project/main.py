# Udemy 100 Projects in 100 days
# Day 19 Project
# TURTLE RACE
# Skills: OOP, Modules, Libraries, Turtle, State
# Notes:

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Who will win? Red, Blue, Green, Yellow, Pink?")
colors = ["red", "orange", "blue", "green", "purple"]
y_positions = [-150, -75, 0, 75, 150]

tmnt = []
for index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.shapesize(3, 3, 3)
    new_turtle.goto(x=-230, y=y_positions[index])
    tmnt.append(new_turtle)

race_over = False
while not race_over:
    mover = random.choice(tmnt)
    mover.forward(random.randint(0, 10))
    if round(mover.xcor(), 0) >= 150:
        race_over = True
        winner = mover.pencolor()
        print(f"{winner} came first!!")
        if winner.lower == bet:
            print("You win!!!!!!")
        else:
            print("You lost")

screen.exitonclick()
