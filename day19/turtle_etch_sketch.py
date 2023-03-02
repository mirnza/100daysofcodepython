from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_clockwise():
    tim.right(10)

def rotate_anticlockwise():
    tim.left(10)

def clear_back():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def listen():
    screen.listen()
    screen.onkey(key= "w", fun= move_forwards)
    screen.onkey(key= "s" , fun= move_backwards)
    screen.onkey(key = "d", fun=rotate_clockwise)
    screen.onkey(key= "a", fun=rotate_anticlockwise)
    screen.onkey(key="c", fun=clear_back)



listen()
screen.exitonclick()