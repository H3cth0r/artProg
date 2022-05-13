"""Game:        Paint - Freegames
Programmer 1:   Luis Angel Gonzalez Tapia
Programmer 2:   Hector Miranda Garcia
Date:           9 / may / 2022
Description:    Program that displays a window where the user is
                able to use some commands with his keyboard for
                actioning different drawing methods and colors.
                The basic functionality was made by the Freegames
                authors, but we added functionality to missing
                functions, the following: the yellow color was
                added; draw circle function was completed; the
                function for drawing a rectangle was completed
                and function for drawing a triangle was also
                completed.
"""

from turtle import *
from turtle import circle as cr # Importing Circle method
from freegames import vector

import math  # Lib imported for sqrt for distance between points


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    # loop for each corner of the square
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end.
       This function uses the circle method from the
       turtle library. We create the distance var
       that calculates the distance between two points
       for defining radius; uses the start to end 
       proints.
    """
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    dis_between_points = math.sqrt((end.x - start.x)**2
                                    + (end.y - start.y)**2) # Calculating radius
    cr(dis_between_points) # Circle func from turtle
    end_fill()


def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    dis_between_points = math.sqrt((end.x - start.x)**2
                                    + (end.y - start.y)**2) # Calculating distance between pointh

    # Statement in case distance between points 
    # In x axis are larger (base).
    if (end.x + start.x) >= (end.y + start.y):
        forward(dis_between_points)
        left(90)
        forward(dis_between_points / 2)
        left(90)
        forward(dis_between_points)
        left(90)
        forward(dis_between_points / 2)
        left(90)
        end_fill()

    # Altitud larger than base statement
    else:
        forward(dis_between_points / 2)
        left(90)
        forward(dis_between_points)
        left(90)
        forward(dis_between_points / 2)
        left(90)
        forward(dis_between_points)
        left(90)
        end_fill()       


def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Loop that will be repeated for each corner.
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start' : None,
         'shape' : line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()

# Definition of colors and correspoding activation keys
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')   # Definition of yellow color

# Definition of figures and corresponding activation keys
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
