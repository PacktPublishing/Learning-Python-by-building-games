class Bird:
    def about(self):
        print("Species: Bird")
    def Dance(self):
        print("Not all but some birds can dance")

class Peacock(Bird):
    def Dance(self):
        print("Peacock can dance")
class Sparrow(Bird):
    def Dance(self):
        print("Sparrow can't dance")
