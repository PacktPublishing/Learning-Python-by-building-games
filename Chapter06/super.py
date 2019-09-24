class Bike:
    def __init__(self):
        print("Bike is starting..")
    def Ride(self):
        print("Riding...")

class Suzuki(Bike):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        Bike().__init__()
