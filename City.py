from Coordinate.CityCoordinate import CityCoordinate
from Buildings.Residential import *
from Buildings.Utility import *


class City:
    def __init__(self, data):
        self.possible_residentials = []
        self.possible_utilities = []
        self.residentials = []
        self.utilities = []
        sorted_information = City.__make_city(self, data)
        city_info = str(sorted_information[0]).split()
        self.rows = int(city_info[0])
        self.columns = int(city_info[1])
        self.distance = int(city_info[2])
        self.possible_residentials = City.sort_buildings(self.possible_residentials)
        self.possible_utilities = City.sort_buildings(self.possible_utilities)
        self.city = []

    def build(self):
        for i in range(self.rows):
            self.city.append([])
            for j in range(self.columns):
                point = CityCoordinate(i, j, 0, None)
                self.city[i].append(point)

        found = False
        counter = 0
        first_building = None
        while not found:
            if self.possible_residentials[counter].size > self.distance:
                first_building = self.possible_residentials[counter]
                found = True
            counter += 1

        self.__make_square(first_building, [0, 0])


        print()

    def __check_building_possibility(self, building, row, column):
        for i in range(row, row + building.rows):
            if i >= self.rows:
                return False
            else:
                for j in range(column, column + building.columns):
                    if j >= self.columns:
                        return False
                    else:
                        if self.city[i][j].content == '#':
                            return False
        return True

    def __make_square(self, residential, top_left_corner):
        row = top_left_corner[0]
        column = top_left_corner[1]
        counter = 0

        while row < self.rows or counter < 3:
            column = top_left_corner[1]
            for _ in range(3):
                if column < self.columns:
                    if self.__check_building_possibility(residential, row, column):
                        column += residential.columns
                        # build residential

        pass

    def set_info(self, columns):
        self.columns = columns

    def __make_city(self, city_data):
        city_info = [city_data[0]]

        def parse_building(data):

            build_info = []
            construction_building = []
            project_counter = 0

            for index_element in range(1, len(data)):
                if data[index_element][0] == 'R' or data[index_element][0] == 'U':
                    length = data[index_element][2]
                    build_info.append([data[index_element], project_counter])
                    project_counter += 1
                    temporary_lst = data[int(index_element + 1):int(index_element) + 1 + int(length)]
                    construction_building.append(temporary_lst)
            return [build_info, construction_building]

        new = parse_building(city_data)
        result = city_info + new

        for build in range(len(new[0])):

            info_about_building = new[0][build]

            construction = new[1][build]

            if info_about_building[0][0] == 'R':
                new_build = Residential(info_about_building, construction)
                self.possible_residentials.append(new_build)
            else:
                new_build = Utility(info_about_building, construction)
                self.possible_utilities.append(new_build)

        return result

    @staticmethod
    def sort_buildings(buildings):
        if buildings[0].type == 'R':
            return sorted(buildings, key=lambda a: a.profit, reverse=True)
        else:
            return sorted(buildings, key=lambda a: a.service_type, reverse=True)
        # return sorted(buildings, key=lambda a: (a.size, a.capacity))

    def get_score(self):
        score = 0
        for r in self.residentials:
            score += r.capacity * len(r.utilities_around)
