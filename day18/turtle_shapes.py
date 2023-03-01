from turtle import Turtle, Screen

tim = Turtle()
def triangle():
    tim.color("blue")
    for _ in range(3):
        tim.forward(100)
        tim.right(120)

def square():
    tim.color("red")
    for _ in range(4):
        tim.forward(100)
        tim.right(90)

def  pentagon():
    tim.color("green")
    for _ in range(5):
        tim.forward(100)
        tim.right(72)

def hexagon():
    tim.color("grey")
    for _ in range(6):
        tim.forward(100)
        tim.right(60)

def heptagon():
    tim.color("pink")
    for _ in range(7):
        tim.forward(100)
        tim.right(51.4285714)  

def octagon():
    tim.color("purple")
    for _ in range(8):
        tim.forward(100)
        tim.right(360/8)     

def nonagon():
    tim.color("cyan")
    for _ in range(9):
        tim.forward(100)
        tim.right(360/9)

def decagon():
    tim.color("magenta")
    for _ in range(10):
        tim.forward(100)
        tim.right(360/10)

def hendecagon():
    tim.color("yellow")
    for _ in range(11):
        tim.forward(100)
        tim.right(360/11)

def dodecagon():
    tim.color("orange")
    for _ in range(12):
        tim.forward(100)
        tim.right(360/12)
triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()
hendecagon()
dodecagon()
screen = Screen()
screen.exitonclick()