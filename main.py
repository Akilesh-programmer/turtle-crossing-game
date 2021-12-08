# With this screen class only we will be able to display the things.
from turtle import Screen
# We are using the time class to make computer delay for a specific time. In other words it can be also said as sleep.
import time
from player import Player
from cars import Cars
from random import randint
from scoreboard import Level, Score

NUMBERS = [0, 1]

screen = Screen()
# Setting the screen size to 600 / 600 pixels.
screen.setup(600, 600)

# The following method can be used to turn off the animations. We can use the screen.update() method to update the screen only when we want so that we can cut out all the unwanted animations.
screen.tracer(0)
game_is_on = True

# Creating the turtle.
turtle = Player()

level1 = Level()
score1 = Score()


# With this function we ca listen to the keystrokes from the user and then assign some function to that.
screen.listen()
# Assigning function to the up arrow key so that it moves upward.
# First creating the function.
def up():
    turtle.move()
# Assigning function to the key.
screen.onkey(key="Up", fun=up)


# Storing all the cars generated in a list.
cars_generated = []

# Creating a variable to store the current level in which the player is playing.
level = 0
# Creating a variable to divide the number of times running.

# Creating a function to generate cars and then make them go to a position.
def generate_cars():
    new_car = Cars()
    new_car.goto(280, randint(-250, 280))
    cars_generated.append(new_car)

score = 0

# We are creating one variable called divider. With this only we are going to divide the times running, and the for each level speed will be varying, so as the level increases divider will be decreasing and that many cars will be generated. If we don't have the divider then at the start lot of cars will be generated and at the last level when the speed is very high cars will be created but distance between the cars will be very huge. First for each 5 running of the loop cars will be generated. As the level increases, that is the speed increases, we will reduce this divider so that with less number of running of loops itself cars will be generated. If you still don't understand this thing then just run the game without changing the divider as the level and speed of the car increases.
divider = 5
times_running = 0
changing_speed = 0

def game():
    global game_is_on
    global times_running
    global level
    global divider
    global changing_speed
    global score
    


    times_running += 1
    screen.update()
    time.sleep(0.1)
    
    

    # Moving the cars.
    for car in cars_generated:
        car.move()
    
    # Detecting collision with the end wall by the turtle.
    if turtle.ycor() >= 280:
        if level < 3:
            score1.clear()
            score += 1
            if score % 3 == 0:
                level += 1
                divider -= 1
                # Increasing the speed of cars.
                changing_speed += 1
                for car in cars_generated:
                    car.move_distance += 5
                level1.clear()
        else:
            score1.clear()
            score += 1
        

        turtle.restart()

    
        
    
    # Generating cars. Generating cars only after 5 times of running of while loop so that we can make the moving smooth and also add spaces between all the cars so that there will be spaces in between.
    if times_running % divider == 0:
        generate_cars()

    

    # Detecting collisions of cars with the turtle.
    for car in cars_generated:
        if car.distance(turtle) < 20:
            game_is_on = False
            

    


while game_is_on:
    game()
    
    level1.write_score(level + 1)
    score1.write_score(score)


    # We are changing the speed of the cars in the function of game itself. But actually it is not updating if we call the function once again. So that again defining the speed.
    if changing_speed == 0:
        for car in cars_generated:
            car.move_distance = 5
    elif changing_speed == 1:
        for car in cars_generated:
            car.move_distance = 10
    elif changing_speed == 2:
        for car in cars_generated:
            car.move_distance = 15
    else:
        for car in cars_generated:
            car.move_distance = 20

    


    

    
# After one comple game resetting all the values and making the code ready for the next game.
times_running = 0
level = 1
divider = 5
changing_speed = 0
changing_speed = 0

# With this method we will be also make the screen object stay on our display until we click on it.
screen.exitonclick()