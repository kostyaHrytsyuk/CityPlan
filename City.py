from Coordinate.CityCoordinate import CityCoordinate
from Buildings.Residential import *
from Buildings.Utility import *
import copy


class City:
    def __init__(self, data):
        self.possible_residentials = []
        self.possible_utilities = []
        self.residentials = {}
        self.utilities = {}
        sorted_information = City.__make_city(self, data)
        city_info = str(sorted_information[0]).split()
        self.rows = int(city_info[0])
        self.columns = int(city_info[1])
        self.distance = int(city_info[2])
        self.possible_residentials = City.sort_buildings(self.possible_residentials)
        self.possible_utilities = City.sort_buildings(self.possible_utilities)
        self.city = []
        self.curr_proj_id = 0

    def build(self):
        for i in range(self.rows):
            self.city.append([])
            for j in range(self.columns):
                point = CityCoordinate(i, j, 0, None)
                self.city[i].append(point)

        found = False
        counter = 0
        first_building = None
        while not found and counter < len(self.possible_residentials):
            if self.possible_residentials[counter].size > self.distance:
                first_building = self.possible_residentials[counter]
                found = True
            counter += 1
        if not found:
            first_building = self.possible_residentials[0]

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
        counter = 0

        while row < self.rows and counter < 3:
            column = top_left_corner[1]
            for _ in range(3):
                if column < self.columns:
                    if self.__check_building_possibility(residential, row, column):
                        if counter == 1 and _ == 1:
                            column += residential.columns * 2
                        else:
                            self.__build_house(residential, [row, column])
                            column += residential.columns
            row += residential.rows
            counter += 1

        print()

    def __build_house(self, house, top_left_corner):
        project = copy.deepcopy(house)
        project.left_top_corner = top_left_corner
        project.coordinates = project.mathematical()
        project.id = self.curr_proj_id
        self.curr_proj_id += 1

        for i in range(project.rows):
            for coordinate in project.coordinates[i]:
                coordinate.id = project.id
                coordinate.build_type = project.type
                coordinate.project_number = project.project_number
                self.city[coordinate.point[0]][coordinate.point[1]] = coordinate

        if project.type == 'R':
            self.look_around(project)
            self.residentials.update({project.id: project})
        else:
            self.look_around(project)
            self.utilities.update({project.id: project})

    def look_around(self, project):
        edge1_lst = project.coordinates[0]
        edge2_lst = []
        edge3_lst = []
        for i in range(len(project.coordinates)):
            edge2_lst.append(project.coordinates[i][0])
            edge3_lst.append(project.coordinates[i][project.columns - 1])
        edge4_lst = project.coordinates[project.rows - 1]
        edges = [edge1_lst, edge2_lst, edge3_lst, edge4_lst]

        for edge in edges:
            for point in edge:
                if point.content == '#':
                    self.find_buildings(point, project)

    def find_buildings(self, coordinate, project):
        self.look_up(coordinate, project)

    def look_up(self, coordinate, project):
        cur_point = coordinate.point
        cur_point[0] -= self.distance
        cur_step = ((coordinate.point[0] - cur_point[0]) - self.distance) + 1
        while cur_point[0] != coordinate.point[0]:
            if 0 <= cur_point[0] < self.rows:
                for column in range(cur_step):
                    if column < self.columns:
                        spot = self.city[cur_point[0]][cur_point[1]]
                        if coordinate.build_type != spot.build_type:
                            if coordinate.content == 'R' and not project.is_utility_around(spot.service_type):
                                project.utilities_around.append(spot.service_type)
                            elif coordinate.content == 'U':
                                neighbour = self.residentials[coordinate.id]
                                if not neighbour.is_utility_around(project.service_type):
                                    neighbour.utilities_around.append(project)
                        cur_point[1] += 1
            cur_point[0] += 1
            cur_point[1] = coordinate.point[1]
            cur_step += 1

    def look_right(self, coordinate, project):
        cur_point = coordinate.point
        cur_point[1] += self.distance
        cur_step = ((coordinate.point[1] - cur_point[1]) - self.distance) + 1
        while cur_point[1] != coordinate.point[1]:
            if cur_point[1] < self.columns:
                for row in range(cur_step):
                    if row < self.rows:
                        spot = self.city[cur_point[0]][cur_point[1]]
                        if coordinate.build_type != spot.build_type:
                            if coordinate.content == 'R' and not project.is_utility_around(spot.service_type):
                                project.utilities_around.append(spot.service_type)
                            elif coordinate.content == 'U':
                                neighbour = self.residentials[coordinate.id]
                                if not neighbour.is_utility_around(project.service_type):
                                    neighbour.utilities_around.append(project)
                        cur_point[0] += 1
            cur_point[0] = coordinate.point[0]
            cur_point[1] -= 1
            cur_step += 1

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

            # info_about_building = new[0][build]
            info_about_building = new[0][build][0].split() + [new[0][build][1]]

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
