import turtle
from turtle import Turtle

def setup_window():
    global wn
    turtle.setup(800,800)
    wn = turtle.Screen()
    wn.title("Title Here")
    wn.bgcolor("slategrey")

def setup_turtle():
    global tu
    tu = Turtle()
    tu.color("teal")
    tu.pensize(3)
    # tu.shape("circle")

def move():
    tu.forward(1)
    wn.ontimer(move, 1000)

setup_window()
setup_turtle()
wn.ontimer(move,1000)
tu.

turtle.mainloop()