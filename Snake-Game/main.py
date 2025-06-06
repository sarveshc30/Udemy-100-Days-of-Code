from turtle import Screen
from Snake import Snekk, Food, Score

#Initializing Screen Obj
snekk = Snekk()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
snekk.create_snekk()
food = Food()
score = Score()
game_on = True

while game_on:
    snekk.move()
    screen.update()
    if snekk.snekk[0].distance(food) < 15:
        snekk.ate_shit()
        food.is_eaten()
        score.scored()

    if snekk.ded:
        score.reset()
        game_on = False

screen.exitonclick()
