from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.speed("fastest")
        self.goto(0, 360)
        self.hideturtle()
        self.refresh_score()

    def increase_score(self):
        self.score += 1

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
