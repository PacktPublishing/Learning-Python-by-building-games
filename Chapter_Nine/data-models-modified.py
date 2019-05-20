class Base:
    def __init__(self, first):
        self.first = first

    def __add__(self, other):
        print(self.first + other.first)
        
