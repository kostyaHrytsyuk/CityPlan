from collections import OrderedDict

from Coordinate.CityCoordinate import CityCoordinate
from Coordinate.CityCoordinateUtility import CityCoordinateUtility
from Buildings.Residential import *
from Buildings.Utility import *
import copy


def null_coordinate(coordinate):
    coordinate.id = None
    coordinate.content = 0
    coordinate.build_type = None


class City:
    def __init__(self, data):
        self.possible_residentials = []
        self.possible_utilities = []
        self.residentials = {}
        self.utilities = []
        sorted_information = City.__make_city(self, data)
        city_info = str(sorted_information[0]).split()
        self.rows = int(city_info[0])
        self.columns = int(city_info[1])
        self.distance = int(city_info[2])
        self.possible_residentials = sorted(self.possible_residentials, key=lambda a: a.profit, reverse=True)
        self.possible_utilities = City.sort_buildings(self.possible_utilities)
        self.mock_project = Building(['U', 1, 1, None, -1], '#')
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

        row = 0
        while row < self.rows:
            column = 0
            while column < self.columns:
                column += self.__make_square(first_building, [row, column])
            row += first_building.rows * 3
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
        cur_point = top_left_corner[:]
        row = cur_point[0]
        counter = 0

        while row < self.rows and counter < 3:
            column = cur_point[1]
            for _ in range(3):
                if column < self.columns:
                    if self.__check_building_possibility(residential, row, column):
                        if counter == 1 and _ == 1:
                            column += residential.columns
                        else:
                            self.__build_house(residential, [row, column])
                            column += residential.columns
            row += residential.rows
            counter += 1
        cur_point[0] += residential.rows
        cur_point[1] += residential.columns
        self.__fill_square_with_utilities(cur_point, residential)
        return residential.columns * 3

    def __fill_square_with_utilities(self, top_left_corner, square_element):
        cur_point = top_left_corner
        for row in range(top_left_corner[0], (top_left_corner[0] + square_element.rows)):
            if row < self.rows:
                cur_point[1] = top_left_corner[1]
                for column in range(top_left_corner[1], (top_left_corner[1] + square_element.columns)):
                    if column < self.columns and self.city[row][column].content != '#':
                        best_utility = self.__find_best_utility([row, column])
                        if best_utility:
                            self.__build_house(best_utility, [row, column])

    def __find_best_utility(self, top_left_corner):
        # TODO: Rewrite neighbour search
        self.mock_project.left_top_corner = top_left_corner[:]
        self.mock_project.coordinates = self.mock_project.mathematical('U')
        coordinate = self.mock_project.coordinates[0][0]
        coordinate.build_type = self.mock_project.type
        coordinate.id = self.mock_project.id
        self.city[top_left_corner[0]][top_left_corner[1]] = coordinate
        neighbour = self.look_around(self.mock_project, True)
        null_coordinate(self.city[top_left_corner[0]][top_left_corner[1]])
        if neighbour:
            u = list(self.possible_utilities.keys())[0]
            while u <= len(self.possible_utilities.keys()):
                if not neighbour.is_utility_around(u):
                    for utility in self.possible_utilities[u]:
                        if self.__check_building_possibility(utility, top_left_corner[0], top_left_corner[1]):
                            return utility
                u += 1
            else:
                return None

    def __build_house(self, house, top_left_corner):
        # info = [house.type, house.rows, house.columns, house.capacity, house.project_number, house.structure]
        # project = Residential(house)
        project = copy.deepcopy(house)
        project.left_top_corner = top_left_corner[:]
        project.coordinates = project.mathematical(project.type)
        project.id = self.curr_proj_id
        self.curr_proj_id += 1

        for i in range(project.rows):
            for coord in project.coordinates[i]:
                if project.type == 'U':
                    point = coord.point
                    coord = CityCoordinateUtility(point[0], point[1], coord.content, None, project.service_type)
                coord.build_type = project.type
                coord.project_number = project.project_number
                coord.id = project.id
                self.city[coord.point[0]][coord.point[1]] = coord

        self.look_around(project)
        if project.type == 'R':
            self.residentials.update({project.id: project})
        else:
            self.utilities.append(project)

    def look_around(self, project, return_value=False):
        edge_up = project.coordinates[0]
        edge_right = []
        edge_left = []
        for i in range(len(project.coordinates)):
            edge_left.append(project.coordinates[i][0])
            edge_right.append(project.coordinates[i][project.columns - 1])
        edge_down = project.coordinates[project.rows - 1]

        for point in edge_up:
            if point.content == '#':
                if not return_value:
                    self.look_left(point, project)
                    self.look_up(point, project)
                    self.look_right(point, project)
                else:
                    res = self.look_left(point, project, return_value)
                    if res:
                        return res
                    res = self.look_up(point, project, return_value)
                    if res:
                        return res
                    res = self.look_right(point, project, return_value)
                    if res:
                        return res

        for point in edge_right:
            if point.content == '#':
                if not return_value:
                    self.look_right(point, project)
                    self.look_down(point, project)
                else:
                    res = self.look_right(point, project, return_value)
                    if res:
                        return res
                    res = self.look_down(point, project, return_value)
                    if res:
                        return res

        for point in edge_down:
            if point.content == '#':
                if not return_value:
                    self.look_down(point, project)
                    self.look_left(point, project)
                else:
                    res = self.look_down(point, project, return_value)
                    if res:
                        return res
                    res = self.look_left(point, project, return_value)
                    if res:
                        return res

        for point in edge_left:
            if point.content == '#':
                if not return_value:
                    self.look_left(point, project)
                else:
                    res = self.look_left(point, project, return_value)
                    if res:
                        return res

    def look_up(self, coord, project, return_value=False):
        res = None
        cur_point = coord.point[:]
        cur_point[0] -= self.distance
        cur_step = ((coord.point[0] - cur_point[0]) - self.distance) + 1
        while cur_point[0] != coord.point[0]:
            if 0 <= cur_point[0]:
                for column in range(cur_step):
                    if cur_point[1] < self.columns:
                        res = self.check_builds_around(coord, cur_point, project, res, return_value)
                        cur_point[1] += 1
            cur_point[1] = coord.point[1]
            cur_point[0] += 1
            cur_step += 1
        return res

    def look_right(self, coord, project, return_value=False):
        res = None
        cur_point = coord.point[:]
        cur_point[1] += self.distance
        cur_step = ((cur_point[1] - coord.point[1]) - self.distance) + 1
        while cur_point[1] != coord.point[1]:
            if cur_point[1] < self.columns:
                for row in range(cur_step):
                    if cur_point[0] < self.rows:
                        res = self.check_builds_around(coord, cur_point, project, res, return_value)
                        cur_point[0] += 1
            cur_point[0] = coord.point[0]
            cur_point[1] -= 1
            cur_step += 1
        return res

    def look_down(self, coord, project, return_value=False):
        res = None
        cur_point = coord.point[:]
        cur_point[0] += self.distance
        cur_step = ((cur_point[0] - coord.point[0]) - self.distance) + 1
        while cur_point[0] != coord.point[0]:
            if cur_point[0] < self.rows:
                for column in range(cur_step):
                    if cur_point[1] >= 0:
                        res = self.check_builds_around(coord, cur_point, project, res, return_value)
                        cur_point[1] -= 1
            cur_point[1] = coord.point[1]
            cur_point[0] -= 1
            cur_step += 1
        return res

    def look_left(self, coord, project, return_value=False):
        res = None
        cur_point = coord.point[:]
        cur_point[1] -= self.distance
        cur_step = ((coord.point[1] - cur_point[1]) - self.distance) + 1
        while cur_point[1] != coord.point[1]:
            if cur_point[1] >= 0:
                for rows in range(cur_step):
                    if cur_point[0] >= 0:
                        res = self.check_builds_around(coord, cur_point, project, res, return_value)
                        cur_point[0] += 1
            cur_point[0] = coord.point[0]
            cur_point[1] += 1
            cur_step += 1
        return res

    def check_builds_around(self, coord, cur_point, project, res, return_value):
        spot = self.city[cur_point[0]][cur_point[1]]
        if spot.content != 0 and spot.content != '.' and coord.id != spot.id and coord.build_type != spot.build_type:
            if coord.build_type == 'R' and not project.is_utility_around(spot.service_type):
                project.utilities_around.append(spot.service_type)
            elif coord.build_type == 'U':
                neighbour = self.residentials[spot.id]
                if not return_value:
                    if not neighbour.is_utility_around(project.service_type):
                        neighbour.utilities_around.append(project.service_type)
                else:
                    res = neighbour
        return res

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
                    length = data[index_element].split()[1]
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
    def sort_buildings(utilities):
        res = {}
        for utility in utilities:
            if utility.service_type not in res:
                res.update({utility.service_type: [utility]})
            else:
                res[utility.service_type].append(utility)
        res = OrderedDict(sorted(res.items(), key=lambda t: t[0]))
        for service_type in res:
            items = res[service_type]
            res[service_type] = sorted(items, key=lambda u: u.size)
        return res

    def get_score(self):
        score = 0
        for r in self.residentials:
            score += self.residentials[r].capacity * len(self.residentials[r].utilities_around)
        return score
