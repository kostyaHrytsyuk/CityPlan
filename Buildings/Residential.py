from Buildings.Building import *


class Residential(Building):

    def __init__(self, general_information, structure):
        super().__init__(general_information, structure)
        self.capacity = general_information[6]
        self.utilities_around = []

    def is_utility_around(self, utility):
        for u in self.utilities_around:
            if utility.service_type == u.service_type:
                return True
        return False
