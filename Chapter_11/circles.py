import pygame as game
from pygame.locals import QUIT
from random import randint
import sys
game.init()
display_screen = game.display.set_mode((650, 470), 0, 32)
while True:
    for eachEvent in game.event.get():
        if eachEvent.type == QUIT:
            sys.exit()
    circle_generate_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    circle_position_arbitary = (randint(0, 649), randint(0, 469))
    circle_radius_arbitary = randint(1, 230)
    game.draw.circle(display_screen, circle_generate_color,
                     circle_position_arbitary, circle_radius_arbitary)
    game.display.update()
