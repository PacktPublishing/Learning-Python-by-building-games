from pygame.locals import *
from random import randint
import pygame
import time
from operator import *

class Player:
    x = [0]
    y = [0]
    size = 44
    direction = 0
    length = 3

    MaxAllowedMove = 2
    updateMove = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[0] = 1 * 44
        self.x[0] = 2 * 44

    def update(self):

        self.updateMove = self.updateMove + 1
        if gt(self.updateMove, self.MaxAllowedMove):

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.size
            if self.direction == 1:
                self.x[0] = self.x[0] - self.size
            if self.direction == 2:
                self.y[0] = self.y[0] - self.size
            if self.direction == 3:
                self.y[0] = self.y[0] + self.size

            self.updateMove = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))



class Computer:
    x = [0]
    y = [0]
    size = 44
    direction = 0
    length = 3

    MaxAllowedMove = 2
    updateMove = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[0] = 1 * 44
        self.y[0] = 4 * 44

    def update(self):

        self.updateMove = self.updateMove + 1
        if gt(self.updateMove, self.MaxAllowedMove):

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.size
            if self.direction == 1:
                self.x[0] = self.x[0] - self.size
            if self.direction == 2:
                self.y[0] = self.y[0] - self.size
            if self.direction == 3:
                self.y[0] = self.y[0] + self.size

            self.updateMove = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def target(self, dx, dy):
        if gt(self.x[0] ,  dx):

            self.moveLeft()

        if lt(self.x[0] , dx):
            self.moveRight()

        if self.x[0] == dx:
            if lt(self.y[0] , dy):
                self.moveDown()

            if gt(self.y[0] , dy):
                self.moveUp()

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))


class Game:
    def checkCollision(self, x1, y1, x2, y2, blockSize):
        if ge(x1 , x2) and le(x1 , x2 + blockSize):
            if ge(y1 , y2) and le(y1, y2 + blockSize):
                return True
        return False


class Frog:
    x = 0
    y = 0
    size = 44

    def __init__(self, x, y):
        self.x = x * self.size
        self.y = y * self.size

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class App:
    Width = 800
    Height = 600
    player = 0
    Frog = 0

    def __init__(self):
        self._running = True
        self.surface = None
        self._image_surf = None
        self._Frog_surf = None
        self.game = Game()
        self.player = Player(5)
        self.Frog = Frog(8, 5)
        self.computer = Computer(5)

    def loader(self):
        pygame.init()
        self.surface = pygame.display.set_mode((self.Width, self.Height), pygame.HWSURFACE)

        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()
        self._Frog_surf = pygame.image.load("frog-main.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def main(self):
        self.computer.target(self.Frog.x, self.Frog.y)
        self.player.update()
        self.computer.update()

        # does snake eat Frog?
        for i in range(0, self.player.length):
            if self.game.checkCollision(self.Frog.x, self.Frog.y, self.player.x[i], self.player.y[i], 44):
                self.Frog.x = randint(2, 9) * 44
                self.Frog.y = randint(2, 9) * 44
                self.player.length = self.player.length + 1

        # does computer eat Frog?
        for i in range(0, self.player.length):
            if self.game.checkCollision(self.Frog.x, self.Frog.y, self.computer.x[i], self.computer.y[i], 44):
                self.Frog.x = randint(2, 9) * 44
                self.Frog.y = randint(2, 9) * 44
                #to increase length
                # self.computer.length = self.computer.length + 1

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.game.checkCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                print( "You lose! ")
                exit(0)

        pass

    def renderer(self):
        self.surface.fill((0, 0, 0))
        self.player.draw(self.surface, self._image_surf)
        self.Frog.draw(self.surface, self._Frog_surf)
        self.computer.draw(self.surface, self._image_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def handler(self):
        if self.loader() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False

            self.main()
            self.renderer()

            time.sleep(50.0 / 1000.0);
        self.on_cleanup()


if __name__ == "__main__":
    main = App()
    main.handler()
