from Buildings.Building import *


class Residential(Building):

    def __init__(self, general_information, structure, top_left_corner=None):
        super().__init__(general_information, structure, top_left_corner)
        self.capacity = int(general_information[3])
        self.profit = self.capacity/self.size
        self.utilities_around = []

    def is_utility_around(self, utility_type):
        if len(self.utilities_around) != 0:
            if utility_type in self.utilities_around:
                return True
        return False

    def get_copy(self, top_left_corner):
        info = [self.type, self.rows, self.columns, self.capacity, self.project_number]
        copy = Residential(info, self.structure, top_left_corner)
        return copy
