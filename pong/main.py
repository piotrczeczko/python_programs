from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()


screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong v1.0")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# right_paddle = Paddle()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "a")

# screen.onkey(right_paddle.up, "Up")
# screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    do_accelerate = False
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.add_r_score()

    # Detect L paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.add_l_score()



screen.exitonclick()
