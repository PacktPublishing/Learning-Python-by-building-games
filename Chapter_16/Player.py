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
