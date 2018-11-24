class Building:
    def __init__(self, general_information, structura):
        self.type = general_information[0]
        self.rows = general_information[1]
        self.columns = general_information[2]
        self.structure = []
        self.save_structure(structura)

    def save_structure(self, struct):
        for i in struct:
            self.structure.append(i[:-1])

    def draw(self):
        pass

    def corect(self):
        pass
