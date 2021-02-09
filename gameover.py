from turtle import Turtle

class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "bold"))