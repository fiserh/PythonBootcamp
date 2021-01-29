import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Race", prompt="color?")
color = ["red","blue"]
y_position = [-70, 70]

turtles = []

for turtle_index in range(len(y_position)):
    new_t = t.Turtle(shape="turtle")
    new_t.color(color[turtle_index])
    new_t.penup()
    new_t.goto(x=-230, y=y_position[turtle_index])
    turtles.append(new_t)

if user_bet:
    is_race_on = True

while is_race_on:
    for _ in turtles:
        _.forward(random.randint(0, 10))
        if _.xcor() == 250:
            is_race_on = False

screen.exitonclick()

# def move_fw():
#     tim.forward(100)
#
#
# def move_bw():
#     tim.backward(100)
#
# def rot_right():
#     tim.setheading(tim.heading()-10)
#
# def rot_left():
#     tim.setheading(tim.heading()+10)
#
#
# screen.listen()
# screen.onkey(move_fw, "w")
# screen.onkey(move_bw, "s")
# screen.onkey(rot_right, "a")
# screen.onkey(rot_left, "d")
# screen.exitonclick()

# directions = [0, 90, 180, 270]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         dashed_line_forward(tim, 10)
#         tim.speed(100000)
#         tim.right(angle)
#
#
# def rand_walk(turtle_object, total_len):
#     turtle_object.speed(100)
#     turtle_object.width(10)
#     for _ in range(total_len):
#         dashed_line_forward(turtle_object, 1)
#         turtle_object.right(random.choice(directions))
#         rand_colour(turtle_object)
#
#
# def rand_colour(turtle_object):
#     colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
#                "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#     turtle_object.color(random.choice(colours))
#
#
# def dashed_line_forward(turtle_object, n):
#     for i in range(n):
#         turtle_object.forward(15)
#         turtle_object.penup()
#         turtle_object.forward(5)
#         turtle_object.pendown()
#
#
# def shape_side(turtle_object, x, y):
#     for shape_side_n in range(x, y):
#         rand_colour(tim)
#         draw_shape(shape_side_n)
#
#
# shape_side(tim, 3, 5)
# rand_walk(tim, 1000)
