from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=y_cor)
    def start_again(self):
        self.goto(STARTING_POSITION)
