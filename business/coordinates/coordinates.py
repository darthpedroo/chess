from business.coordinates.i_coordinates import ICoordinates


class Coordinates(ICoordinates):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coordinates(self) -> tuple[int, int]:
        return self.x, self.y
