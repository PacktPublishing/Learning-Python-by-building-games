class Bike:
    def __init__(self):
        print("Bike is starting..")
    def Ride(self):
        print("Riding...")

class Suzuki(Bike):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def info(self):
        print("You are riding {} and it's color is {}".format(self.name,self.color))
