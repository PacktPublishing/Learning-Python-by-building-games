class Bike:
    name = ''
    color= ' '
    price = 0
    
    def info(self, name, color, price):
        self.name, self.color, self.price = name,color,price
        print("{}: {} and {}".format(self.name,self.color,self.price))
