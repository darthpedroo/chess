from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates


class MovementOneUp(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(1, 0))
        return movements


class MovementOneDown(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(-1, 0))
        return movements


class MovementOneLeft(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(0, -1))
        return movements


class MovementOneRight(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(0, 1))
        return movements


class MovementOneTopLeft(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(-1, -1))
        return movements


class MovementOneTopRight(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(-1, 1))
        return movements


class MovementOneBackwardsLeft(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(1, -1))
        return movements


class MovementOneBackwardsRight(MovementPattern):

    def get_posible_movements(self):
        movements = []
        movements.append(Coordinates(1, 1))
        return movements
