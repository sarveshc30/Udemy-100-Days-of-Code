import turtle
from turtle import Turtle
import random


def rand_walk(num_walk, angle):
    tim = Turtle()
    tim.speed(8)
    tim.width(5)
    num = int(360 / angle)
    tim.screen.colormode(255)
    for i in range(num_walk + 1):
        tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.forward(30)
        turn = angle * random.randint(1, num)
        tim.right(turn)

    turtle.Screen().exitonclick()


rand_walk(90, 60)
