import sys
import pygame as p  # abbreviating pygame module as p
from pygame.locals import QUIT, KEYDOWN, FULLSCREEN, K_f

p.init()
displayScreen = p.display.set_mode((640, 480), 0, 32)
displayFullscreen = False
while True:
    for Each_event in p.event.get():
        if Each_event.type == QUIT:
            sys.exit()
        if Each_event.type == KEYDOWN:
            if Each_event.key == K_f:
                displayFullscreen = not displayFullscreen
                if displayFullscreen:
                    displayScreen = p.display.set_mode((640, 480), FULLSCREEN,
                                                       32)
                else:
                    displayScreen = p.display.set_mode((640, 480), 0, 32)
    p.display.update()
