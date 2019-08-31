class Speed:
    def __init__(self, speed=0):
        self.set_speed(speed)

    def change_to_mile(self):
        return (self.get_speed * 0.6213, "miles")


# new updates are made as follows using getter and setter

    def get_speed(self):

        return self._speed

    def set_speed(self, km):
        if km > 50:
            raise ValueError("You are liable to speed ticket")
        self._speed = km
