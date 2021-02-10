import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MAXCARS = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")

cars = []

INCREMENTAL_SPEED = 0.1

game_is_on = True
while game_is_on:

    for car in range(random.randint(0,1)):
        new= CarManager()
        cars.append(new)

    for cari in cars:
        cari.move()
        if cari.distance(player)<1:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        score.increase_score()
        score.refresh_score()
        player.refresh()


    time.sleep(INCREMENTAL_SPEED)
    screen.update()

screen.exitonclick()