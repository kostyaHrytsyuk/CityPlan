class City:
    def __init__(self, data):
        self.rows = data[0]
        self.columns = data[2]
        self.distance = data[4]

        self.possible_building = []

    def build(self):
        pass

    def setInfo(self, columns):
        self.columns = columns
