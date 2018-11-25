from Buildings.Building import *


class Residential(Building):

    def __init__(self, general_information, structure):
        super().__init__(general_information, structure)
        self.capacity = general_information[6]
