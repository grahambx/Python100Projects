# Udemy 100 Projects in 100 days
# Day 20 Project
# PONG
# Skills: OOP, Turtle, Event, Time, Inheritance
# Notes:

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
new_round_direction = [1, 1]
while game_is_on:
    time.sleep(ball.move_speed)   # tying this to an attribute of ball, which is increased on paddle hit
    ball.move()
    screen.update()
    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()

    # detect left miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()


screen.exitonclick()

