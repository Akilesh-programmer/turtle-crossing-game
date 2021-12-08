from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        
    def write_score(self, level):
        self.write(f"Level: {level} ", move=False, align='left', font=('Courier', 25, 'normal'))

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 220)
        
    def write_score(self, score):
        self.write(f"Score: {score}", move=False, align='left', font=('Courier', 25, 'normal'))