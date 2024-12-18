from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates


class MovementLeft(MovementPattern):

    def get_posible_movements(self):

        movements = []
        for i in range(7):
            mov = i + 1
            movements.append(Coordinates(0, -mov))

        return movements
