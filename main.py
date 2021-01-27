import turtle as t
import random

tim = t.Turtle()

directions = [0, 90, 180, 270]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        dashed_line_forward(tim, 10)
        tim.speed(100000)
        tim.right(angle)


def rand_walk(turtle_object, total_len):
    turtle_object.speed(100)
    turtle_object.width(10)
    for _ in range(total_len):
        dashed_line_forward(turtle_object, 1)
        turtle_object.right(random.choice(directions))
        rand_colour(turtle_object)


def rand_colour(turtle_object):
    colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
               "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    turtle_object.color(random.choice(colours))


def dashed_line_forward(turtle_object, n):
    for i in range(n):
        turtle_object.forward(15)
        turtle_object.penup()
        turtle_object.forward(5)
        turtle_object.pendown()


def shape_side(turtle_object, x, y):
    for shape_side_n in range(x, y):
        rand_colour(tim)
        draw_shape(shape_side_n)


shape_side(tim, 3, 5)
rand_walk(tim, 1000)
