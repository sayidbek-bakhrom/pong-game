from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()

  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
    ball.bounce_x()

  if ball.distance(left_paddle) < 50 and ball.xcor < -320:
    ball.bounce_x()

  if ball.xcor() > 380:
    ball.reset_postion()
  
  if ball.xcor() < -380:
    ball.reset_postion()


screen.exitonclick
