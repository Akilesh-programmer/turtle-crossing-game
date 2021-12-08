from turtle import Turtle
STARTING_POSITION = (0, -280)
# Creating a class for the turtle that we are going to use for the game.
class Player(Turtle):

    def __init__(self):
        super().__init__()
        # This method takes the pen up from the turlte so that it won't draw line when we move it.
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # Creating a method to move the turtle.
    def move(self):
        self.forward(10)

    def restart(self):
        self.goto(STARTING_POSITION)


