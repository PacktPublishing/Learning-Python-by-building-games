class Mobile:
    def __init__(self):
        print("Mobile features: Camera, Phone, Applications")
class Samsung(Mobile):
    def __init__(self):
        print("Samsung Company")
        super().__init__()
class Samsung_Prime(Samsung):
    def __init__(self):
        print("Samsung latest Mobile")
        super().__init__()
