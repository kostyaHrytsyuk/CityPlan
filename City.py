from Residential import *
from Utility import *


class City:
    def __init__(self, data):
        self.possible_residentials = []
        self.possible_utilities = []
        sorted_information = City.__make_city(self, data)
        self.rows = int(sorted_information[0][0])
        self.columns = int(sorted_information[0][2])
        self.distance = int(sorted_information[0][4])

    def build(self):
        pass

    def set_info(self, columns):
        self.columns = columns

    def __make_city(self, city_data):
        city_info = [city_data[0]]

        def parse_building(data):

            build_info = []
            construction_building = []

            for index_element in range(1, len(data)):
                if data[index_element][0] == 'R' or data[index_element][0] == 'U':
                    length = data[index_element][2]
                    build_info.append(data[index_element])
                    temporary_lst = data[int(index_element + 1):int(index_element) + 1 + int(length)]
                    construction_building.append(temporary_lst)
            return [build_info, construction_building]

        new = parse_building(city_data)
        result = city_info + new

        for build in range(len(new[0])):

            info_about_building = new[0][build]

            construction = new[1][build]

            if info_about_building[0] == 'R':
                new_build = Residential(info_about_building, construction)
                if new_build.correct:
                    self.possible_residentials.append(new_build)
            else:
                new_build = Utility(info_about_building, construction)
                if new_build.correct:
                    self.possible_utilities.append(new_build)

        return result
