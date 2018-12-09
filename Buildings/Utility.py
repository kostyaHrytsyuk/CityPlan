from Buildings.Building import *


class Utility(Building):

    def __init__(self, general_information, structure):
        super().__init__(general_information, structure)
        self.service_type = int(general_information[3])
