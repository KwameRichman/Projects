import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
#tim.pensize(2)
tim.speed("fastest")
radius = 100
# Creating Random RBG Colours
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, b, g)

    return colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)


screen = Screen()
screen.exitonclick()