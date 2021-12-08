from turtle import Turtle
from random import randint

COLORS = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# Creating a cars class to create cars.
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.move_distance = 5
        self.penup()
        self.goto(0, 0)
        self.color_number = randint(0, 6)
        self.color(COLORS[self.color_number])
        self.speed("slowest")

    # Creating a method to move the cars.
    def move(self):
        self.backward(self.move_distance)
        
        