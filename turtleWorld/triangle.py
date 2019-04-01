import turtle
from turtle import Turtle


def draw_triangle(t, x1, y1, x2, y2, x3, y3, color):
    t.fillcolor(color)
    t.begin_fill()
    t.penup()
    t.goto(x1,y1)
    #move the t to x1,y1

    #draw the triangle
    t.pendown()
    t.goto(x2,y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    t.end_fill()

def main():
    Austin = Turtle()

    draw_triangle(Austin,0,0,100,0,0, -100 ,"green")

    turtle.done()
main()