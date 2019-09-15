def target(self, dx, dy):
    if gt(self.x[0], dx):

        self.moveLeft()

    if lt(self.x[0], dx):
        self.moveRight()

    if self.x[0] == dx:
        if lt(self.y[0], dy):
            self.moveDown()

        if gt(self.y[0], dy):
            self.moveUp()
