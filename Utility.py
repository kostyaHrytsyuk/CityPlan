from Building import *


class Utility(Building):

    def __init__(self, general_information, structure):
        super().__init__(general_information, structure)
        self.service_type = general_information[6]
