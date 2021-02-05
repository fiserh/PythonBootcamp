import turtle as t
import time

screen = t.Screen()
screen.setup(width=500, height=400, )
screen.bgcolor("black")

start_shape = [(0, 0), (20, 0), (40,0), (60,0)]

segments = []

for pos in start_shape:
    newseg = t.Turtle()
    newseg.color("white")
    newseg.shape("square")
    newseg.penup()
    newseg.goto(pos)
    segments.append(newseg)

def terin():
    if screen.onkeypress() == "w":
        return tur.forward(20)
    elif screen.onkeypress() == "s":
        return tur.backward(20)
    elif screen.onkeypress() == "d":
        return tur.right(20)
    elif screen.onkeypress() == "a":
        return tur.left(20)
    else:
        return tur.forward(20)



gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.5)

    for seg in range(len(segments)-1, 0 ,-1):
        newx = segments[seg - 1].xcor()
        newy = segments[seg -1 ].ycor()
        segments[seg].goto(newx, newy)

    terin(segments[0])





# for _ in start_shape:
#     a = t.Turtle("square")
#     a.color("white")
#     a.goto(_)
#     segments.append(a)
#
# new_shape=[]
#
# for _ in range(len(start_shape)):
#     tup = start_shape[-_-1][0], start_shape[-_-1][1] + 20*_U
#     new_shape.append(tup)
#
# for _ in new_shape:
#     a = t.Turtle("square")
#     a.color("white")
#     a.goto(_)
#     segments.append(a)


screen.exitonclick()
