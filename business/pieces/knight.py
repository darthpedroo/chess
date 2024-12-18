from business.pieces.piece import Piece
from business.movement_patterns.movement_knight import MovementKnight


class Knight(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.movement_patterns = [MovementKnight()]
