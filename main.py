import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400, )

screen.bgcolor("black")

turtles = []

tim = t.Turtle()
tim.shape("circle")
tim.color("white")
tim.pensize()
tim.pensize(20)
tim.speed(1)

start_shape = [(0, 0), (-20, 0), (-40,0)]

segments = []

for _ in start_shape:
    a = t.Turtle("square")
    a.color("white")
    a.goto(_)
    segments.append(a)

new_shape=[]

for _ in range(len(start_shape)):
    tup = start_shape[-_-1][0], start_shape[-_-1][1] + 20*_
    new_shape.append(tup)

for _ in new_shape:
    a = t.Turtle("square")
    a.color("white")
    a.goto(_)
    segments.append(a)


screen.exitonclick()
