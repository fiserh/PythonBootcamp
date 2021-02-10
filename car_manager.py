from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=3)
        self.setheading(90)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.goto(random.randint(-300,300), 0)
        self.speed("fast")
         
    def move(self):
            self.forward(20)
    
