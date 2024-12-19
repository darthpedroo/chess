from business.pieces.piece import Piece
from business.movement_patterns.movement_one import (
    MovementOneUp,
    MovementOneDown,
    MovementOneLeft,
    MovementOneRight,
    MovementOneBackwardsRight,
    MovementOneBackwardsLeft,
    MovementOneTopLeft,
    MovementOneTopRight,
)


class King(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.movement_patterns = [
            MovementOneUp(),
            MovementOneDown(),
            MovementOneLeft(),
            MovementOneRight(),
            MovementOneBackwardsLeft(),
            MovementOneBackwardsRight(),
            MovementOneTopLeft(),
            MovementOneTopRight(),
        ]
