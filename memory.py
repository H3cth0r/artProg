"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
# Atributos para el puntaje
writer = Turtle(visible=False)
forma = {'score': 0}



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        #Se suma el puntaje cada vez que estar correcto
        forma['score'] += 1
         


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        """Here we are setting spaces for each case
           of number length. We set some properties
           for centering each number in each tile.
        """
        x, y = xy(mark)
        up()
        goto(x + 2, y + 7)
        color('black')
        if len(str(tiles[mark])) == 1:
            num_tile = "  " + str(tiles[mark])
            write(num_tile,font=('Arial', 20, 'normal'))
        elif tiles[mark] >= 20:
            num_tile = " " + str(tiles[mark])
            write(num_tile, align="left",font=('Arial', 20, 'normal'))
        else:
            num_tile = " " + str(tiles[mark])
            write(num_tile,font=('Arial', 20, 'normal'))
    #Se dibuja el score 
    writer.write(forma['score'])
    writer.goto(190, 185)
    writer.color('green')

    if forma['score'] == 32:
        writer.goto(0, 0)
        writer.write("Terminaste")
        
    

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
