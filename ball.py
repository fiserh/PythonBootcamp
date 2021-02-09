from turtle import Turtle
import random

MOVE_DIST = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.setheading(45)
        self.shape("circle")
        self.color("white")
        self.xcor = random.randint(-300,300)
        self.ycor = random.randint(-300, 300)
        self.goto(self.xcor, self.ycor)
        self.direction = 0

    def move(self):
        if self.direction == 0:
            self.forward(20)
        else:
            self.backward(20)

    def change_direction(self):
        if self.direction == 0:
            self.direction = 1
        elif self.direction == 1:
            self.direction =0