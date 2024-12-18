from business.coordinates.i_coordinates import ICoordinates


class Coordinates(ICoordinates):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Coordinates"):
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other_coordinates: "Coordinates"):

        x, y = other_coordinates.get_coordinates()
        return Coordinates(self.x + x, self.y + y)

    def __str__(self):
        coords = (self.x, self.y)
        return str(coords)

    def get_coordinates(self) -> tuple[int, int]:
        return self.x, self.y
