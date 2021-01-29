import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400, )

screen.bgcolor("black")

turtles = []

tim = t.Turtle()
tim.shape("square")
tim.color("white")
tim.pensize()
tim.pensize(20)

start_shape = [(0, 0), (0, 20)]

for _ in range(len(start_shape)):
    tim.setpos(start_shape[_])


screen.exitonclick()
