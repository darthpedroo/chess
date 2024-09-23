from abc import ABC
from colors import COLORS


class Piece(ABC):
    def __init__(self,fen_notation_piece: str):
        self._fen_notation_piece = fen_notation_piece
        self._color = self._get_piece_color()

    def _get_piece_color(self):
        if self._fen_notation_piece.upper() == self._fen_notation_piece:
            return COLORS["WHITE"]
        return COLORS["BLACK"]
        
class Pawn(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)
    
class Rook(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)

class Knight(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)

class Bishop(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)

class Queen(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)

class King(Piece):
    def __init__(self, fen_notation_piece: str):
        super().__init__(fen_notation_piece)




