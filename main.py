import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import GameOver

screen = t.Screen()
screen.setup(width=500, height=400, )
screen.bgcolor("black")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.5)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        score.refresh_score()

    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 180 or snake.head.ycor() < -180:
        overgame = GameOver()
        gameOn = False


screen.exitonclick()
