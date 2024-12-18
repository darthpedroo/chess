from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates

class MovementOneUp(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(1,0))
        return movements
    