import turtle as t
import time
from ball import  Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width=800, height=800 )
screen.bgcolor("black")

paddle1 = Paddle()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    paddle1.move()
    ball.move()

    if paddle1.distance(ball) < 30:
        ball.change_direction()
        score.increase_score()
        score.refresh_score()

    if paddle1.ycor() > 360:
        paddle1.down()
    elif paddle1.ycor() < -360:
        paddle1.up()

    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce()

    if ball.xcor() < - 360:
        ball.change_direction()

    if ball.xcor() > 380:
        ball.refresh()


screen.exitonclick()
