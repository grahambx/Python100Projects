from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.level_start()

    def level_start(self):
        """moves player to start for each level"""
        self.goto(STARTING_POSITION)

    def move(self):
        """makes player move forward"""
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        """checks if player has made it to finish line"""
        if self.ycor() >= FINISH_LINE_Y:
            return True
