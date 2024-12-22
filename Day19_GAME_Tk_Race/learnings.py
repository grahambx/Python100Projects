# Udemy 100 Projects in 100 days
# Day 19 Learning
# ETCH-A-SKETCH
# Skills: OOP, Modules, Libraries, Turtle, Event Handling, Event Listening
# Notes:

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(15)


def turn_left():
    tim.left(15)


def screen_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# don't need a loop here, the event listeners will listen until screen.exitonclick()

screen.onkey(key="w", fun=move_forwards)  # Note we are passing in a function name, not calling it, so no ()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=screen_clear)


screen.exitonclick()
print("b")
