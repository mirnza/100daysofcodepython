import turtle as t
import random
tim = t.Turtle()

tim.width(5)
directions = [0, 90, 180, 270]
tim.speed("fastest")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()

    tim.color(R,G,B)



def random_movement():
    for _ in range(200):
        tim_forward = random.random()
        change_color()
        tim.forward(55*tim_forward)
        tim.setheading(random.choice(directions))

random_movement()
screen = t.Screen()
screen.exitonclick()



