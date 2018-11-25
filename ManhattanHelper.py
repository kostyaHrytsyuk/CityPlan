class ManhattanHelper:

    @staticmethod
    def manhattan_distance(a, b):
        x = abs(a[0] - b[0])
        y = abs(a[1] - b[1])
        return x + y
