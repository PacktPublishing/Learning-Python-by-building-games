class Bike:
    __name = " "
    __color = " "
    def __init__(self,name,color):
        self.__name = name
        self.__color = color
    def setNewColor(self, color):
        self.__color = color
    def info(self):
        print("{} is of {} color".format(self.__name,self.__color))
