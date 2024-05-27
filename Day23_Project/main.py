# Udemy 100 Projects in 100 days
# Day 23 Project Capstone
# TURTLE CROSSING GAME
# Skills: OOP, Turtle, Event, Time, Inheritance
# Notes: Capstone = coded up without guidance

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Turtle Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.game_speed)
    screen.update()
    scoreboard.write_score()
    car_manager.create_car()
    car_manager.move_cars()

    # check for player to hit finish line
    if player.finish_line():
        scoreboard.new_level()
        player.level_start()
        scoreboard.game_speed *= 0.9
        car_manager.reset_cars()

    # check for collision
    for car in car_manager.cars:
        if abs(car.xcor() - player.xcor()) < 20 and abs(car.ycor() - player.ycor()) < 22:
            scoreboard.end_game()
            game_is_on = False

screen.exitonclick()
