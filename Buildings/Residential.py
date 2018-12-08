from Buildings.Building import *


class Residential(Building):

    def __init__(self, general_information, structure):
        super().__init__(general_information, structure)
        self.capacity = int(general_information[3])
        self.profit = self.capacity/self.size
        self.utilities_around = []

    def is_utility_around(self, utility_type):
        for u in self.utilities_around:
            if utility_type == u.service_type:
                return True
        return False
