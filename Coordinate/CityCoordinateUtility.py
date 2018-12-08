from Coordinate.CityCoordinate import CityCoordinate


class CityCoordinateUtility(CityCoordinate):

    def __init__(self, x, y, content, build_type, service_type):
        super().__init__(x, y, content, build_type)
        self.service_type = service_type
