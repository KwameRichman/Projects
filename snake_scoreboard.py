from turtle import Turtle

FONT = ('Arial', 20, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 315)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT )

    def eaten_food(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)



