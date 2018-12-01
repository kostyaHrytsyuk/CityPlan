from Coordinate.Coordinates import Coordinates


class CityCoordinate(Coordinates):
    def __init__(self, x, y, content, build_type):
        super().__init__(x, y, content)
        self.build_type = build_type
