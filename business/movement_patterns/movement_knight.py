from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates
from business.movement_patterns.movement_patterns import MovementPattern
from business.coordinates.coordinates import Coordinates


class KnightMove1(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(2, 1)]


class KnightMove2(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(2, -1)]


class KnightMove3(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(-2, 1)]


class KnightMove4(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(-2, -1)]


class KnightMove5(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(1, 2)]


class KnightMove6(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(1, -2)]


class KnightMove7(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(-1, 2)]


class KnightMove8(MovementPattern):
    def get_posible_movements(self):
        return [Coordinates(-1, -2)]
