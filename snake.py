"""Game:        Snake - Freegames
Programmer1:    Luis Angel Gonzalez Tapia
Programmar2:    Héctor Miranda García
Date:           9 / may / 2022
Description:    This is a replica of the popular retro game named
                "Snake". Here the user is able to control the game
                character movement; the objective is to make longer 
                the snake by eating some of the food on the map.
                The user wont be able to exit from the square map,
                and wont be able also to cross its own tail.
                For this activity we had to make the food move around
                the map and not to go out of the map; also we had 
                to make that the color of the head and the food to
                change of color each time the game is started over, 
                this in a random way.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

# List of colors for head of snake and food
Colores = ["green", "black", "blue", "yellow", "pink"]

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
ColorFood = choice(Colores)  # Random choice color from list for food
ColorSnake = choice(Colores) # Random choice color from list for snake

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return (-200 < head.x < 190 and -200 < head.y < 190)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)



    if head == food:
        print('Snake:', len(snake))
        
        # Starting position of the food
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:   
        snake.pop(0)
        if inside(food):
            # This makes food move randomly, generating
            # The movement of the food, goes from -1 to 1.
            food.x += randrange(-1, 1) * 5
            food.y += randrange(-1, 1) * 5

        # In case food not inside the map, will be moved to
        # Some plance inside the map.
        elif not inside(food):
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10


    clear()

    for body in snake:
        square(body.x,
               body.y,
               9, 
               ColorSnake) # ramdom choice color snake head

    square(food.x,
           food.y,
           9, 
           ColorFood) # random choice color food
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Instanciating keys that produce movement of character
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
