import turtle
from turtle import Turtle
import time
import random

class Snekk:
    #Creating Snekk
    def __init__(self):
        self.snekk = []
        self.ded = False


    def create_snekk(self):
        xpos = 0
        for i in range(0, 3):
            head = Turtle()
            head.shape('square')
            head.color('white')
            head.penup()
            self.snekk.append(head)
            self.snekk[i].goto(xpos, y=0)
            xpos -= 20


    #Snake Turning Functions
    def right_turn(self):
        if self.snekk[0].heading() != 0 and self.snekk[0].heading() != 180:
            self.snekk[0].setheading(0)

    def left_turn(self):
        if self.snekk[0].heading() != 0 and self.snekk[0].heading() != 180:
            self.snekk[0].setheading(180)

    def up_turn(self):
        if self.snekk[0].heading() != 90 and self.snekk[0].heading() != 270:
            self.snekk[0].setheading(90)

    def down_turn(self):
        if self.snekk[0].heading() != 90 and self.snekk[0].heading() != 270:
            self.snekk[0].setheading(270)


    #Defining Snekk Growth Function
    # noinspection PyShadowingNames
    def ate_shit(self):
        tail = Turtle()
        tail.shape('square')
        tail.color('white')
        tail.penup()
        self.snekk.append(tail)

    def move(self):
        #Game Start and Stop Rules
        turtle.listen()

        #Segment Movement
        time.sleep(0.1)
        prev_positions = []
        for seg in self.snekk:
            prev_positions.append((seg.xcor(), seg.ycor()))

        #Snekk Movement Animation
        self.snekk[0].forward(20)
        for index in range(1, len(self.snekk)):
            self.snekk[index].goto(prev_positions[index-1])
            if self.snekk[0].distance(self.snekk[index]) < 11:
                self.ded = True



        #Direction Control
        turtle.onkeypress(self.right_turn, 'Right')
        turtle.onkeypress(self.left_turn, 'Left')
        turtle.onkeypress(self.up_turn, 'Up')
        turtle.onkeypress(self.down_turn, 'Down')

        #Death





class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.speed('fastest')

    def is_eaten(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.speed('fastest')

    def position(self):
        return self.position

class Score(Turtle):
    def __init__(self):
        self.score = 0
        with open('high_score.txt','r') as file:
            self.highscore = int(file.read())
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 250)
        self.speed('fastest')
        self.write(f'Score: {self.score}, HighScore: {self.highscore}', move=False, align='center', font=('Times New Roman', 16, 'normal'))

    def scored(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}, HighScore: {self.highscore}', move=False, align='center', font=('Times New Roman', 16, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            with open('high_score.txt', 'w') as file:
                file.write(str(self.score))
        self.score = -1
        self.scored()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Times New Roman', 20, 'normal'))


    # def game_over(self):
    #
