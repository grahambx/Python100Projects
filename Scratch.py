from turtle import Turtle, Screen

geoff = Turtle()
roger = Turtle()
sleeves = Turtle()
spokes = Turtle()

mutant_turtles = [geoff, roger, sleeves, spokes]

geoff.color("red")
roger.color("green")
sleeves.color("blue")
spokes.color("purple")

geoff.left(90)
roger.left(180)
sleeves.right(90)

for _ in range(4):
    for turtle in mutant_turtles:
        turtle.turtlesize(3,3,3)
        turtle.forward(100)
        turtle.left(90)

screen = Screen()
screen.exitonclick()