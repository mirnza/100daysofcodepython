from turtle import Turtle, Screen
import random
tim = Turtle()

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R,G,B)

i = 3

while not i == 13:
    change_color()
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)
    
    i += 1

screen = Screen()
screen.exitonclick()


