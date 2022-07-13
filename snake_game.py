import time
from turtle import Screen
from snake_xtics import Snake
from snake_food import Food
from snake_scoreboard import ScoreBoard
from snake_border import Border


screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Kwame's Snake Game")
screen.tracer(0)

# Creates the snake object on screen
snake = Snake()
# Creates the food object on screen
food = Food()
# Creates a score board
scoreboard = ScoreBoard()
# Creates a Borderline
border = Border()


# Controlling the snake by using the listen keyword
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Alternatively
# screen.onkey(key="Right", fun=snake.right)
# screen.onkey(key="Left", fun=snake.left())
# screen.onkey(key="Down", fun=snake.down)
# screen.onkey(key="Up", fun=snake.up)


# The screen is going to update every 0.1 seconds
game_is_on = True
while game_is_on:
    screen.update()  # refresh the screen
    time.sleep(0.2)  # delay for 0.1 seconds

    border.draw_border()
    snake.move()   # move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.eaten_food()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:  # using slicing to slice the list
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
