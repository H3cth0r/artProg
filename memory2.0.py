"""Game:        Memory - Freegames
Programmer1:    Luis Angel Gonzalez Tapia
Programmar2:    Héctor Miranda García
Date:           9 / may / 2022
Description:    This is the version 2.0 of the game momory. 
                As said on the documentation of the first version,
                what we did for this version was to change the values
                under the tiles to be colors, instead of interger
                numbers. Basically is the same as version 1.0, but 
                wit the values under the tiles being colors.
"""






from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Tiles generates a list with 64 integers
# ranging from 0 to 31. When started the
# game, the tiles or numbers in list are
# shuffled.

screen = Screen()
tiles = list(range(32)) * 2 
state = {'mark': None}
hide = [True] * 64

# Atributos para el puntaje
writer = Turtle(visible=False)
forma = {'score': 0}


colors = []
# creating list of colors
for i in range(100):
    random_number = randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = "#" + hex_number[2:]
    if len(hex_number) != 7:
        continue
    else:
        colors.append(hex_number)
colors = list(set(colors))
print(colors)
print("len colors: ", len(colors))
    


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
    shape(car)  # here the car img gets printed
    stamp()


    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        """ Here we'll be changing the numbers
            to be random colors. The generated
            colors are located in the variable
            named "colors"
        """
        x, y = xy(mark)
        up()
        goto(x + 2, y + 7)
        down()
        color('black', colors[int(tiles[mark])])
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()       
    # Score is drawn
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
