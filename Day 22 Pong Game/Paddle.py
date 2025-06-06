from turtle import Turtle
import turtle
class Paddle():
    def __init__(self, xpos):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.speed('fastest')
        self.paddle.color('white')
        self.paddle.goto(x=xpos, y=0)


    def go_up(self):
        ypos = self.paddle.ycor() + 10
        xpos = self.paddle.xcor()
        self.paddle.goto(x=xpos, y=ypos)

    def go_down(self):
        ypos = self.paddle.ycor() - 10
        xpos = self.paddle.xcor()
        self.paddle.goto(x=xpos, y=ypos)

    def move(self):
        turtle.listen()
        turtle.onkeypress(self.go_up, 'Up')
        turtle.onkeypress(self.go_down, 'Down')


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_inc = 2
        self.y_inc = 2

    def move(self):
        new_x = self.xcor() + self.x_inc
        new_y = self.ycor() + self.y_inc
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.y_inc *= -1

    def bounce_y(self):
        self.x_inc *= -1
    