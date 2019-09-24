class Bike:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print("{}: {} and {}".format(self.name,self.color,self.price))
