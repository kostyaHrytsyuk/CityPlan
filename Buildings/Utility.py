from Buildings.Building import *


class Utility(Building):

    def __init__(self, general_information, structure, top_left_corner=None):
        super().__init__(general_information, structure, top_left_corner)
        self.service_type = int(general_information[3])

    def get_copy(self, top_left_corner):
        info = [self.type, self.rows, self.columns, self.service_type, self.project_number]
        copy = Utility(info, self.structure, top_left_corner)
        return copy
