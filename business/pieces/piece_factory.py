from business.pieces.pawn import Pawn


class PieceFactory:
    """Creates pieces"""

    @staticmethod
    def create_piece(nombre: str, color: str):
        return Pawn(nombre, color)
