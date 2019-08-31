class Bike:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print("{0}: {1} and {2}".format(self.name, self.color, self.price))
