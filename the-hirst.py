import random
import turtle
from turtle import Turtle, Screen

colour_list = [(229, 249, 73), (229, 237, 253), (67, 252, 194), (17, 184, 82), (19, 15, 96), (218, 153, 94), (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203), (28, 245, 41), (248, 21, 135), (168, 3, 123), (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243), (172, 92, 13), (11, 92, 180), (64, 114, 247), (183, 183, 250), (183, 2, 1), (249, 21, 18), (53, 98, 1), (76, 248, 252), (4, 181, 187), (19, 151, 58)]


k = Turtle()
turtle.colormode(255)
k.speed("fastest")
k.penup()
k.hideturtle()
# Adjusting the starting point
k.setheading(225)
k.forward(300)
k.setheading(0)


def draw_dot_line():
    for _ in range(10):
        k.dot(20, random.choice(colour_list))
        k.forward(50)


def move_to_next_line():
    k.left(90)
    k.forward(50)
    k.left(90)
    k.forward(500)
    k.setheading(0)


for _ in range(10):
    draw_dot_line()
    move_to_next_line()

screen = Screen()
screen.exitonclick()

