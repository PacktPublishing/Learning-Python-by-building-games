from characters import RoundPig
from polygon import Polygon


class Level():
    def __init__(self, pigs_no, columns_no, beams_no, obj_space):
        self.pigs = pigs_no
        self.columns = columns_no
        self.beams = beams_no
        self.space = obj_space
        self.number = 0
        self.total_number_of_birds = 4

    def build_0(self):

        pig_no_1 = RoundPig(980, 100, self.space)
        pig_no_2 = RoundPig(985, 182, self.space)
        self.pigs.append(pig_no_1)
        self.pigs.append(pig_no_2)
        p = (950, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 240)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4

    def build_1(self):
        """level 1"""
        pig = RoundPig(1000, 100, self.space)
        self.pigs.append(pig)
        p = (900, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1050, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1105, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.total_number_of_birds = 4

    def load_level(self):
        try:
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_" + str(self.number)
            getattr(self, build_name)()
