from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(270, random.randint(-260, 270))
        self.setheading(180)
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        x_cor = self.xcor() - self.speed
        self.goto(x_cor, self.ycor())

    def new_level(self):
        self.speed += MOVE_INCREMENT
