from turtle import Turtle

MOVE_DIST = 20

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.goto(380, 0)
        self.speed("fast")
        self.direction = 0



    def move(self):
        if self.direction == 0:
            self.forward(20)
        else:
            self.backward(20)

    #     newseg.color("white")
    #     newseg.shape("square")
    #     newseg.penup()
    #     newseg.goto(pos)
    #
    # def create_paddle(self):
    #     for pos in START:
    #         self.add_segment(pos)
    #
    # def add_segment(self, pos):
    #     newseg = t.Turtle()
    #     newseg.color("white")
    #     newseg.shape("square")
    #     newseg.penup()
    #     newseg.goto(pos)


    def up(self):
        self.direction = 0

    def down(self):
        self.direction = 1
