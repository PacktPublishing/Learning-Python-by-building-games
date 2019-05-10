class Speed:
    def __init__(self, speed = 0):
        self.speed = speed

    def change_to_mile(self):
        return (self.speed*0.6213," miles")
    
    def get_speed(self):
        return self._speed
    def set_speed(self, km):
        if km > 50:
            raise ValueError("You are liable to speeding ticket")
        self._speed = km
    
    #using property
    speed = property(get_speed,set_speed)
