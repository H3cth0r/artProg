"""Game:        Cannon - Freegames
Programmer1:    Luis Angel Gonzalez Tapia
Programmar2:    Héctor Miranda García
Date:           9 / may / 2022
Description:    This game consist of proyectiles and targets. The
                game is about aming to the targets using the cursor
                and tu calculate the required energy to reach the 
                target. The proyectile follows a parabolic trajectory
                and the user is enabled to shoot a proyectile every
                time there is non other proyectile in the map. For
                this we were requiered to make the proyectile and the
                displacement of the targets to move faster; we were
                also required to make the game to be infinite, meaning
                that the targets must reposition on the window.
"""


from random import random, randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        
        # Changed frequency in which velocity was divided
        # For making the movement faster.
        speed.x = (x + 200) /15
        speed.y = (y + 200) /15


def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # Changed speed of the blue targets.
        target.x -= 2.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # We rearange the target, to make the inifinite game
    for target in targets:
        if not inside(target):
            target.x=200
            target.y=randrange(-150,150)
            


            


    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
