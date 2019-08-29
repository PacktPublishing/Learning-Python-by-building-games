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
