import turtle
import pandas as pd

tim = turtle.Turtle()
screen = turtle.Screen()
screen.title('US States Game')
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')

score = 0
df = pd.read_csv('50_states.csv')
states = list(df['state'])
while(True):
    ans = screen.textinput(title=f'score: {score}', prompt="What's the state name?")

    if ans.title() in states:
        x = int(df['x'][df['state'] == ans.title()])
        y = int(df['y'][df['state'] == ans.title()])
        tim.penup()
        tim.goto(x, y)
        tim.pendown()
        tim.write(ans.title())
        states.remove(ans.title())
        score += 1

