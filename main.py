import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(width=500, height=400, )
screen.bgcolor("black")

snake = Snake()



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
