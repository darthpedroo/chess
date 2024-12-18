from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates


class MovementDiagonal(MovementPattern):

    def get_posible_movements(self):
        movements = []

        for i in range(7):
            mov = i + 1
            movements.append(Coordinates(mov, mov))
            movements.append(Coordinates(mov, -mov))
            movements.append(Coordinates(-mov, mov))
            movements.append(Coordinates(-mov, -mov))
        return movements
