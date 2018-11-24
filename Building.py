class Building:
    def __init__(self, general_information, structura):
        self.type = general_information[0]
        self.rows = general_information[1]
        self.columns = general_information[2]
        self.structure = []
        self.save_structure(structura)
        self.cordinates = self.mathematical()
        # self.correct = self.correct()

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

        structura =[ i for i in self.structure]
        str_structura = ''
        for i in structura:
            str_structura += i

        cordinate = [[i, j] for i in range(len(structura)) for j in range(len(structura[0]))]

        print(str_structura)

        for i in range(len(str_structura)):
            if str_structura[i] == '.':
                cordinate[i].append([0])
            elif str_structura[i] == '#':
                cordinate[i].append([1])

        print(cordinate)

        return cordinate

    def correct(self):
        chk = True
        if chk:
            edge1 = self.structure[0]
            if '#' not in edge1:
                chk = False


        edge2 = 0
        edge3 = 0
        edge4 = 0

        return chk
