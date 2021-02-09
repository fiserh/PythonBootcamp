from turtle import Turtle
import random as r

SIZEX = 230
SIZEY = 180

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cor = r.randint(-SIZEX, SIZEX)
        y_cor = r.randint(-SIZEY, SIZEY)
        self.goto(x_cor, y_cor)
