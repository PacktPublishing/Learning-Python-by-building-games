from pygame.locals import *
from random import randint
import pygame
import time
from operator import *


class Frog:
    x = 0
    y = 0
    size = 44

    def __init__(self, x, y):
        self.x = x * self.size
        self.y = y * self.size

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))
