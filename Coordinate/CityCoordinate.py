from Coordinate.Coordinates import Coordinates


class CityCoordinate(Coordinates):
    def __init__(self, x, y, content, build_type, project_number=0):
        super().__init__(x, y, content)
        self.build_type = build_type
        self.project_number = project_number
