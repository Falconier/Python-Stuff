import datetime
import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800,800)
wn.title("Clock by Ian and Jacob")

global tu
tu = turtle.Turtle()

tu.hideturtle()
tu.speed(0)
tu.pensize(5)

global h,m,s

def drawClock(r,h,m,s):
    tu.penup()
    tu.goto(0,r)
    tu.setheading(180)
    tu.color("gold")
    tu.pendown()
    tu.circle(r)

    tu.penup()
    tu.goto(0,0)
    tu.setheading(90)
    # for i in range(300):
    #     tu.color("lightgreen")
    #     tu.pensize(1)
    #     tu.fd(r-8)
    #     tu.pendown()
    #     tu.fd(8)
    #     tu.penup()
    #     tu.goto(0,0)
    #     tu.rt(1.2)
    for i in range(60):
        tu.color("LemonChiffon")
        tu.pensize(2)
        tu.fd(r-15)
        tu.pendown()
        tu.fd(15)
        tu.penup()
        tu.goto(0,0)
        tu.rt(6)
    for i in range(12):
        tu.color("LemonChiffon")
        tu.pensize(2)
        tu.fd(r-20)
        tu.pendown()
        tu.fd(20)
        tu.penup()
        tu.goto(0,0)
        tu.rt(30)


    drawHourHand(r,h)
    drawMinuteHand(r,m)
    drawSecondHand(r,s)

def drawHourHand(r,h):
    tu.penup()
    tu.goto(0,0)
    tu.color("white")
    tu.setheading(90)
    angle = (h/12)*360
    tu.rt(angle)
    tu.pendown()
    tu.fd(r*.33)

def drawMinuteHand(r,m):
    tu.penup()
    tu.goto(0, 0)
    tu.color("slategrey")
    tu.setheading(90)
    angle = (m / 60) * 360
    tu.rt(angle)
    tu.pendown()
    tu.fd(r*.75)

def drawSecondHand(r,s):
    tu.penup()
    tu.goto(0, 0)
    tu.color("red")
    tu.setheading(90)
    angle = (s/60)*360
    tu.rt(angle)
    tu.pendown()
    tu.fd(r * .9)




while True:
    h = int(time.strftime('%I'))
    m = int(time.strftime("%M"))
    s = int(time.strftime('%S'))

    print(s)
    drawClock(250, h, m, s)
wn.mainloop()
