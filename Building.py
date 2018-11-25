from Coordinates import *


class Building:
    def __init__(self, general_information, structure):
        self.type = general_information[0]
        self.rows = int(general_information[2])
        self.columns = int(general_information[4])
        self.structure = []
        self.save_structure(structure)
        self.coordinates = self.mathematical()
        self.correct = self.correct()

    def save_structure(self, structure):
        for i in range(len(structure)-1):
            self.structure.append(structure[i][:-1])
        var = structure[len(structure)-1][-1]
        if var == '\n':
            self.structure.append(structure[len(structure)-1][:-1])
        else:
            self.structure.append(structure[len(structure) - 1])

    def draw(self):
        print('-----------------')
        for i in self.structure:
            print(i)

    def mathematical(self):
        str_structure = ''
        for i in self.structure:
            str_structure += i

        raw_coordinates = [[i, j] for i in range(len(self.structure)) for j in range(len(self.structure[0]))]

        for i in range(len(str_structure)):
            if str_structure[i] == '.':
                raw_coordinates[i].append(str_structure[i])
            elif str_structure[i] == '#':
                raw_coordinates[i].append(str_structure[i])

        coordinates = []
        for p in raw_coordinates:
            coordinates.append(Coordinates(p[0], p[1], p[2]))

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

    def correct(self):
        if self.check_edges():
            if self.check_neighbours():
                return True
        return False
