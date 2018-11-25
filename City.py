class City:
    def __init__(self, data):
        self.rows = data[0]
        self.columns = data[2]
        self.distance = data[4]
        self.possible_residentials = []
        self.possible_utilities = []

    def build(self):
        pass

    def set_info(self, columns):
        self.columns = columns

    @staticmethod
    def manhattan_distance(a, b):
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])
        return x + y