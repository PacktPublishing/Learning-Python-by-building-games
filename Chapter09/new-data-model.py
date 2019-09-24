class Base:
    def __new__(cls):
        print("This is __new__() magic method")
        obj = object.__new__(cls)
        return obj
    def __init__(self):
        print("This is __init__() magic method")
        self.info = "I love Python"
