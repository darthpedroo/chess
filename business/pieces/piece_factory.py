from business.pieces.pawn import Pawn
from business.pieces.rook import Rook
from business.pieces.knight import Knight
from business.pieces.bishop import Bishop
from business.pieces.queen import Queen
from business.pieces.king import King

class PieceFactory:
    """Creates pieces"""

    @staticmethod
    def create_piece(nombre: str, color: str):
        if nombre == "pawn":
            return Pawn(nombre,color)
        elif nombre == "rook":
            return Rook(nombre,color)
        elif nombre == "knight":
            return Knight(nombre,color)
        elif nombre == "bishop":
            return Bishop(nombre,color)
        elif nombre == "queen":
            return Queen(nombre,color)
        elif nombre == "king":
            return King(nombre,color)
        else:
            raise ValueError(f"Unknown piece type: {nombre}")
