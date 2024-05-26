from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "bold")
GAME_OVER_FONT = ("Courier", 25, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.teleport(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("yellow")
        self.write(arg=f"GAME OVER!!!\n Final score: {self.score}", align=ALIGNMENT, font=GAME_OVER_FONT)