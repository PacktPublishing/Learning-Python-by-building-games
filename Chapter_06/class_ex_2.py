class Bike:
    name = ''
    color = ''
    price = 0

    def info(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        print("{0}: {1} and {2}".format(self.name, self.color, self.price))
