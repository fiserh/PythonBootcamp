from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.setheading(180)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.goto(300,random.randint(-260,260))

    def move(self):
            self.forward(MOVE_INCREMENT)
    
