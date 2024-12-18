from business.pieces.piece import Piece
from business.movement_patterns.movement_diagonal import MovementDiagonal


class Bishop(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.movement_patterns = [MovementDiagonal()]
