import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(8)
tim.speed("fastest")

# Creating Random RBG Colours
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_colour = (r, b, g)

    return rand_colour


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
angle = [90, 180, 270, 0]
distance = 50

count = 0
while count < 201:
    count += 1
    tim.color(random_colour())
    tim.forward(distance)
#    tim.right(random.choice(angle))
    tim.setheading(random.choice(angle))


screen = Screen()
screen.exitonclick()