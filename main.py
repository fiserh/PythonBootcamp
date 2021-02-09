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

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

scoreboard = Scoreboard()

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    paddle1.move()
    ball.move()

    if paddle1.distance(ball) < 30:
        ball.change_direction()

    if paddle1.ycor() > 360:
        paddle1.down()
    elif paddle1.ycor() < -360:
        paddle1.up()

    if ball.
#     if snake.head.distance(food) < 15:
#         snake.extend()
#         food.refresh()
#         score.increase_score()
#         score.refresh_score()
#
#     if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 180 or snake.head.ycor() < -180:
#         overgame = GameOver()
#         gameOn = False
#
#     for seg in snake.segments[1:]:
#         if snake.head.distance(seg) < 15:
#             overgame = GameOver()
#             gameOn = False


screen.exitonclick()
