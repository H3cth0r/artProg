"""Game: Paint
Programmer 1: Luis Angel Gonzalez Tapia
Programmer 2: Héctor Miranda García

Fecha: 9 / mayo / 2022
"""

from turtle import *
from turtle import circle as cr
from freegames import vector
import math


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

    for count in range(4):  # will be looped four times
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    '''Draw circle from start to end.'''
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    dis_between_points = math.sqrt((end.x-start.x)**2
                                    + (end.y-start.y)**2) # calculating raius
    cr(dis_between_points) # circle func from turtle
    end_fill()


def rectangle(start, end):
    '''Draw rectangle from start to end.'''
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    dis_between_points = math.sqrt((end.x-start.x)**2
                                    + (end.y-start.y)**2) # calculating distance between pointh
    if (end.x+start.x) >= (end.y+start.y):  # in case base longer
        forward(dis_between_points)
        left(90)
        forward(dis_between_points/2)
        left(90)
        forward(dis_between_points)
        left(90)
        forward(dis_between_points/2)
        left(90)
        end_fill()
    else:                                   # in case hight is longer
        forward(dis_between_points/2)
        left(90)
        forward(dis_between_points)
        left(90)
        forward(dis_between_points/2)
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
    for count in range(3): # will be repeated three times
        forward(end.x - start.x)
        left(120)   # This is the angle

    end_fill()





def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):  # must be repeated three times
        forward(end.x - start.x)
        left(120)   # must turn on 120 angles

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


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
"Se agrego el color amarillo"
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
