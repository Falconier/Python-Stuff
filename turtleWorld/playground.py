'''
keyeventdemo.py: move the turtle by keys
'''
import sys
import turtle

'''def setup_playground():
    turtle.setup(400, 400)
    playground = turtle.screen()
    playground.title("Playground")
    playground.bgcolor("lightgreen")

    amy = turtle.Turtle()
'''
turtle.setup(400, 400)
playground = turtle.Screen()
playground.title("Playground")
playground.bgcolor("lightgreen")

amy = turtle.Turtle()


def move_forward():
    print("Forward")
    amy.forward(20)


def turn_left():
    amy.left(45)


def turn_right():
    amy.right(45)


# def main():


playground.onkey(move_forward, "Up")
playground.onkey(turn_left, "Left")
playground.onkey(turn_right, "Right")

# listen to the key press event
playground.listen()

turtle.mainloop()

# main()