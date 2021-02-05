import turtle as t

START = [(0, 0), (-20, 0), (-40,0), (-60,0)]
MOVE_DIST = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START:
            newseg = t.Turtle()
            newseg.color("white")
            newseg.shape("square")
            newseg.penup()
            newseg.goto(pos)
            self.segments.append(newseg)

    def move(self):
        for seg in range(len(self.segments)-1, 0 ,-1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg -1 ].ycor()
            self.segments[seg].goto(newx, newy)
        self.head.forward(MOVE_DIST)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
    # def terin():
    #     if screen.onkey("w") == :
    #         return tur.forward(20)
    #     elif screen.onkeypress() == "s":
    #         return tur.backward(20)
    #     elif screen.onkeypress() == "d":
    #         return tur.right(20)
    #     elif screen.onkeypress() == "a":
    #         return tur.left(20)
    #     else:
    #         return tur.forward(20)