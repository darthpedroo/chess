from business.pieces.piece import Piece
from business.movement_patterns.movement_forward import MovementForward
from business.movement_patterns.movement_backwards import MovementBackwards
from business.movement_patterns.movement_left import MovementLeft
from business.movement_patterns.movement_right import MovementRight
from business.movement_patterns.movement_forward_left_diagonal import (
    MovementForwardLeftDiagonal,
)
from business.movement_patterns.movement_forward_right_diagonal import (
    MovementForwardRightDiagonal,
)
from business.movement_patterns.movement_backwards_left_diagonal import (
    MovementBackwardsLeftDiagonal,
)
from business.movement_patterns.movement_backwards_right_diagonal import (
    MovementBackwardsRightDiagonal,
)


class Queen(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.movement_patterns = [
            MovementForward(),
            MovementBackwards(),
            MovementForward(),
            MovementLeft(),
            MovementRight(),
            MovementForwardLeftDiagonal(),
            MovementForwardRightDiagonal(),
            MovementBackwardsLeftDiagonal(),
            MovementBackwardsRightDiagonal(),
        ]
