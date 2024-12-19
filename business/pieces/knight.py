from business.pieces.piece import Piece
from business.movement_patterns.movement_knight import (
    KnightMove1,
    KnightMove2,
    KnightMove3,
    KnightMove4,
    KnightMove5,
    KnightMove6,
    KnightMove7,
    KnightMove8,
)


class Knight(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.movement_patterns = [
            KnightMove1(),
            KnightMove2(),
            KnightMove3(),
            KnightMove4(),
            KnightMove5(),
            KnightMove6(),
            KnightMove7(),
            KnightMove8(),
        ]
