from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.level_is = 1

    def level(self):
        self.penup()
        self.goto(0, 260)
        self.write(f"LEVEL: {self.level_is}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def clear_score(self):
        self.clear()
