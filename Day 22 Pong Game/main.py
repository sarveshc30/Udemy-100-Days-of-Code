from turtle import Screen, Turtle
from Paddle import Paddle
from Paddle import Ball
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')


ball = Ball()
left_paddle = Paddle(-350)
right_paddle = Paddle(350)

while True:
    screen.listen()
    ball.move()
    if ball.ycor() == 300 or ball.ycor() == -300:
        ball.bounce_x()

    if ball.xcor() == 340 or ball.xcor() == -340:
        if ball.distance(left_paddle.paddle) < 100:
            ball.bounce_y()
        if ball.distance(right_paddle.paddle) < 100:
            ball.bounce_y()


    screen.onkeypress(left_paddle.go_up, 'w')
    screen.onkeypress(left_paddle.go_down, 's')
    screen.onkeypress(right_paddle.go_up, 'Up')
    screen.onkeypress(right_paddle.go_down, 'Down')

screen.exitonclick()
