

from math import pi
import turtle
from turtle import Turtle


class Circle:
    def __init__(self, turtleName, x1, y1, r, color):
        self.color = color
        self.radius = r
        self.x1 = x1
        self.y1 = y1
        global t
        t = turtleName

    def drawCircle(self):
        t.color(self.color)
        t.penup()
        t.goto(self.x1, self.y1)
        t.goto(self.x1 + self.radius, self.y1)
        t.lt(90)

        t.pendown()
        count = 0
        while True:
            if (count > 120):
                break
            else:
                t.fd((2.0 * pi * self.radius) / 120)
                t.lt(3)
                count += 1


def main():
    tu = Turtle()

    c = Circle(tu, 0, 0, 100, "red")
    c.drawCircle()
    d = Circle(tu, 100, 100, 50, "green")
    d.drawCircle()
    # drawCircle(tu,0,0,100,"red")

    turtle.done()


main()
