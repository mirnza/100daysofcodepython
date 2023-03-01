import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R,G,B) 

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        change_color()
        tim.circle(100) 
        tim.setheading(tim.heading() + size_of_gap) 

draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

