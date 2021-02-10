STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=3, stretch_wid=1)
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.speed("fastest")
        self.goto(380, 0)
        self.speed("fast")

    def up(self):
        self.direction = 0