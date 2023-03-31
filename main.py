import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "space")

game_is_on = True
round_count = 6
cars = []
while game_is_on:
    scoreboard.level()
    if round_count == 6:
        car_manager = CarManager()
        round_count = 0
        cars.append(car_manager)
    round_count += 1
    for i in range(len(cars)):
        cars[i].move()
        if player.distance(cars[i]) < 25:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor() == 280:
            scoreboard.clear_score()
            cars[i].new_level()
            player.start_again()
            scoreboard.level_is += 1

    time.sleep(0.1)
    screen.update()
screen.exitonclick()
