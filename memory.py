"""Game:        Memory - Freegames
Programmer1:    Luis Angel Gonzalez Tapia
Programmar2:    Hector Miranda Garcia
Date:           9 / may / 2022
Description:    This is a digital version of the popular board game
                called 'Memory'. For this game the user is forced
                and challenged to memorize the location of the values
                under the tiles to find the pairs and encrease his
                score. The board consists of 64 tiles and 32 pairs.
                On this game, the values under the tiles are integer
                numbers, raging from 1 to 32. The user must click under
                the desired tile to uncover its value. Each time the 
                user finds a pair, the tile is "removed" from the board
                and a part of the backgroud on the board gets visible, 
                this way at the end of the game, the user will be able
                to apreciate an image of car as the background of the
                map. For this game, we were required  to do is to 
                count and display the number or taps; detect and display
                a message in case the use has finished; to center the
                digit into the square and to create a copy of this 
                changes, but adding another way of displaying some kind
                of values under the tile. We decided that the second 
                version was going to consist of colors, instead of 
                numbers. You can find this other version here, named
                'memory2.0.py.'
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

        # Se suma el puntaje cada vez que estar correcto
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
            write(num_tile,
                  font=('Arial', 20, 'normal'))
        elif tiles[mark] >= 20:
            num_tile = " " + str(tiles[mark])
            write(num_tile,
                  align="left",
                  font=('Arial', 20,
                  'normal'))
        else:
            num_tile = " " + str(tiles[mark])
            write(num_tile,font=('Arial', 
                                  20,
                                  'normal'))
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
