"""Ant, simple animation demo.

Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)

"""

from random import *
from turtle import *
from base import vector

ant = vector(0, 0)  # ant is character
aim = vector(2, 0)  # aim is next position


def wrap(value):
    "Wrap value around -200 and 200."
    return value  # TODO


def draw():
    "Move ant and draw screen."
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

    aim.move(random() - 0.5)
    aim.rotate(random() * 10 - 5)

    clear()
    goto(ant.x, ant.y)
    dot(10)

    if running:
        ontimer(draw, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
running = True
draw()
done()
