import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Pong!")
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.tracer(0)

r_paddle = Paddle((280, 0))
l_paddle = Paddle((-280, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 250 or ball.distance(l_paddle) < 50 and ball.xcor() < -250:
        ball.bounce_x()

    # Detect if ball has left bounds of screen
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
