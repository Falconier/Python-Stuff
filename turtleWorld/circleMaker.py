from math import pi, sin, cos
import turtle
from turtle import Turtle


def drawCircle(t, x1, y1, r, color):
    t.fillcolor(color)
    t.penup()
    t.goto(x1, y1)

    t.begin_fill
    t.pendown()
    t.circle(r)
    t.end_fill

    t.penup()
    t.goto(x1, y1 - (2 * r))
    t.pendown()
    count = 0
    while (count < 360):
        t.forward(2)
        t.left(1)
        count = count + 1


def main():
    tu = Turtle()

    drawCircle(tu, 0, 0, 100, "red")

    turtle.done()


main()
