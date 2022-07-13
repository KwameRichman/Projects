from turtle import Turtle


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

    def draw_border(self):
        self.goto(-310, -310)
        for i in range(4):
            self.pendown()
            self.forward(620)
            self.left(90)
