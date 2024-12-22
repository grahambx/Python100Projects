# Udemy 100 Projects in 100 days
# Day 18 Project
# FROG DRAWING
# Skills: OOP, Modules, Libraries, Turtle, Cologram, Tuple
# Notes:

import random
import turtle as t                  # import the full library, only needed like this to change library level colormode
from turtle import Turtle, Screen   # import specific Class components from a Library
import colorgram

# change the library level colormode setting to support RGB tuples
t.colormode(255)


def rgb_list(input_colors):
    """convert cologram output to a list of RGB tuples"""
    rgb_colors = []
    for item in input_colors:
        r = item.rgb.r
        g = item.rgb.g
        b = item.rgb.b
        rgb = (r, g, b)
        rgb_colors.append(rgb)
    return rgb_colors


def get_random_color():
    """generate a random RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(turtle):
    """draws overlapping shapes from 3 to 10 sides"""
    sides = 3
    while sides <= 10:
        angle = 360 / sides
        turtle.color(get_random_color())
        for _ in range(sides):
            turtle.forward(100)
            turtle.left(angle)
        sides += 1


def random_walk(turtle):
    """draws a random walk, with random colours/distances/directions"""
    for _ in range(10000):
        turtle.color(get_random_color())
        turtle.forward(random.randint(1, 100))
        turtle.left(random.randint(1, 360))


def make_spiro(turtle, gap_size):
    """draw a spirograph where gap_size is the rotation between circles"""
    for _ in range(int(360 / gap_size)):
        turtle.color(get_random_color())
        turtle.circle(200)
        turtle.setheading(turtle.heading() + gap_size)


def make_hirst(turtle):
    """creates a damian hirst like drawing"""
    turtle.penup()
    turtle.pensize(50)
    turtle.teleport(-450, -450)
    # extract colors from hirst painting into list of rgb tuples using colorgram
    extract_colors = colorgram.extract('200430102527-01-damien-hirst-severed-spots.jpg', 6)
    rgb_options = rgb_list(extract_colors)
    print(rgb_options)
    y_axis = -450
    for _ in range(8):
        y_axis += 100
        turtle.teleport(-450, y_axis)
        for _ in range(8):
            turtle.color(random.choice(rgb_options))
            turtle.pendown()
            turtle.forward(0)
            turtle.penup()
            turtle.forward(100)



geoff = Turtle()
geoff.turtlesize(3, 3, 3)
geoff.speed(5)
geoff.pensize(5)

# below, uncomment the option you want to run.

make_spiro(geoff, 10)
# draw_shape(geoff)
# random_walk(geoff)
# make_hirst(geoff)

screen = Screen()
screen.exitonclick()


