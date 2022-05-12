"""Game: Snake
 programmer 1: Luis Angel Gonzalez Tapia
 programmer 2: H�ctor Miranda Garc�a
 Date: 11/05/2022
"""


"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

""" Created this list of colors for the snake and food"""
Colores = ["green", "black", "blue", "yellow", "pink"]
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
ColorFood=choice(Colores) # random choice color from list for food
ColorSnake=choice(Colores) # random choice color from list for snake

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


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
        
        """Starting position of food"""
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:   
        snake.pop(0)
        if inside(food):
            """making foot move on random range
            from -1 to 1
            """
            food.x += randrange(-1, 1) * 5
            food.y += randrange(-1, 1) * 5
        elif not inside(food):
            """In case the food moves outside of
            the map, the food will be place in
            another ramdom place of the map.
            """
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10


    clear()

    for body in snake:
        square(body.x, body.y, 9, ColorSnake) # ramdom choice color snake head

    square(food.x, food.y, 9, ColorFood) # random choice color food
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
