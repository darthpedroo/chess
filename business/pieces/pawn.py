from business.pieces.piece import Piece
from business.movement_patterns.movement_one import MovementOneUp
from business.movement_patterns.movement_one import MovementOneDown


class Pawn(Piece):

    def __init__(self, name, color):
        super().__init__(name, color)
        if self.color == "black":
            self.movement_patterns = [MovementOneUp()]
        else:
            self.movement_patterns = [MovementOneDown()]
