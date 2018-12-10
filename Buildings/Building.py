from Coordinate.Coordinates import *
from Coordinate.CityCoordinate import CityCoordinate
from ManhattanHelper import *


class Building:
    def __init__(self, general_information, structure, left_top_corner=None):
        if left_top_corner is None:
            left_top_corner = [0, 0]
        self.type = general_information[0]
        self.rows = int(general_information[1])
        self.columns = int(general_information[2])
        self.structure = structure
        self.left_top_corner = left_top_corner
        self.project_number = general_information[4]
        if left_top_corner:
            self.coordinates = self.mathematical(self.type)
        else:
            self.coordinates = self.mathematical()
        self.size = self.get_building_size()
        self.id = None

    def draw(self):
        for i in self.structure:
            print(i)

    def mathematical(self, build_type=None):
        bld_model = []
        counter = 0
        for i in range(self.left_top_corner[0], self.left_top_corner[0] + len(self.structure)):
            bld_model.append([])
            for j in range(self.left_top_corner[1], self.left_top_corner[1] + len(self.structure[0])):
                bld_model[counter].append([i, j])
            counter += 1

        for i in range(len(self.structure)):
            j = 0
            for char in self.structure[i]:
                if char == '.':
                    bld_model[i][j].append(char)
                elif char == '#':
                    bld_model[i][j].append(char)
                j += 1

        coordinates = []
        for row in range(len(bld_model)):
            coordinates.append([])
            for q in range(len(bld_model[row])):
                data = [bld_model[row][q][0], bld_model[row][q][1], bld_model[row][q][2]]
                if build_type:
                    coordinates[row].append(CityCoordinate(data[0], data[1], data[2], build_type))
                else:
                    coordinates[row].append(Coordinates(data[0], data[1], data[2]))

        return coordinates

    def check_edges(self):
        edge1_lst = self.structure[0]
        edge2_lst = ''
        edge3_lst = ''
        for i in range(len(self.structure)):
            edge2_lst += self.structure[i][0]
            edge3_lst += self.structure[i][self.columns - 1]
        edge_lst4 = self.structure[self.rows - 1]

        def cor(data):
            return True if '#' in data else False

        chk = False

        if cor(edge1_lst):
            if cor(edge2_lst):
                if cor(edge3_lst):
                    if cor(edge_lst4):
                        chk = True
        return chk

    def check_neighbours(self):
        neighbours = []
        for i in range(len(self.structure)):
            for j in range(self.columns-1):
                if i-1 >= 0:
                    up = self.structure[i-1][j]
                    neighbours.append(up)
                if j-1 >= 0:
                    left = self.structure[i][j-1]
                    neighbours.append(left)
                if i+1 < self.rows:
                    bot = self.structure[i+1][j]
                    neighbours.append(bot)
                if j+1 < self.columns:
                    right = self.structure[i][j+1]
                    neighbours.append(right)

                if '#' not in neighbours:
                    return False
        return True

    def __correct(self):
        if self.check_edges():
            if self.check_neighbours():
                return True
        return False

    def get_building_size(self):
        a = self.coordinates[0][0].point
        b = self.coordinates[-1][-1].point
        if a == b == [0, 0]:
            size = 1
        else:
            size = ManhattanHelper.manhattan_distance(a, b)
        return size
