from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.game_speed = 0.1

    def write_score(self):
        """maintains scoreboard in top left"""
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def new_level(self):
        """increments level number"""
        self.level += 1

    def end_game(self):
        """sets end game state & outcome"""
        game_over = Turtle()
        game_over.hideturtle()
        game_over.write(arg="GAME\nOVER", align="center", font=FONT)