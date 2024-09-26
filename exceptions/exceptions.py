class TileNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Tile Not Found")


class TileHasNoPiece(Exception):
    def __init__(self) -> None:
        super().__init__("Tile Has No Piece")

class TileHasPiece(Exception):
    def __init__(self) -> None:
        super().__init__("Tile Has Piece")
