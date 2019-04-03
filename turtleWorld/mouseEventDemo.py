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
    tu.color("crimson")
    tu.pensize(3)
    # tu.shape("circle")

def move(x,y):
    tu.goto(x,y)

def clear():
    tu.clear()

def move2(x,y):
    tu.penup()
    tu.goto(x,y)
    tu.pendown()

def story_time():
    setup_window()
    setup_turtle()
    wn.onclick(move,1)
    wn.onkey(clear,"c")
    wn.onclick(move2,3)
    # wn.onkeyrelease(tu.pendown(),"p")
    wn.listen()
    turtle.mainloop()

def main():
    story_time()

main()