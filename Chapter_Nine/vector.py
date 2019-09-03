class Vector(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other
        return "(%s, %s)" % (self.x, self.y)

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return "(%s, %s)" % (self.x, self.y)

    def __imul__(self, other):
        if isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return "(%s, %s)" % (self.x, self.y)

    def __itruediv__(self, other):
        if isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return "(%s, %s)" % (self.x, self.y)

    def __mul__(self, scalar):
        return (self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return (self.x / scalar, self.y / scalar)

    def __neg__(self, value):
        return (-self.x, -self.y)

    def __eq__(self, other):
        # v.__eq__(w) -> v == w
        # >>> v = Vector(1, 2)
        # >>> w = Vector(1, 2)
        # >>> v == w
        # True

        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented
