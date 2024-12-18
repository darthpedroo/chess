from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates


class MovementKnight(MovementPattern):

    def get_posible_movements(self):

        movements = [
            Coordinates(2, 1),
            Coordinates(2, -1),
            Coordinates(-2, 1),
            Coordinates(-2, -1),
            Coordinates(1, 2),
            Coordinates(1, -2),
            Coordinates(-1, 2),
            Coordinates(-1, -2),
        ]
        return movements
