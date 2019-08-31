class Bike:
    __name = " "
    __color = " "

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def info(self):
        print("{0} is of {1} color".format(self.__name, self.__color))
