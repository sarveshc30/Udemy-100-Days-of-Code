import turtle
from turtle import Turtle
import random

colors = []
sides = int(input('enter a number:'))
tim = Turtle()
tim.pendown()
tim.pensize(5)
tim.screen.colormode(255)
for i in range(3, sides+1):
    angle = 360/i
    tim.pencolor((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
    for j in range(i):
        tim.forward(100)
        tim.right(angle)


turtle.Screen().exitonclick()
