from abc import ABC
from fen import Fen
from tile import Tile
from piece import Rook, Knight, Bishop, Queen, King, Pawn
from exceptions import InvalidFenNotation
from collections.abc import Iterator
from board_drawer import BoardIteratorOneMatrix, BoardIteratorColumnRow


class BoardBuilder(ABC):


    def build_board(self):
        raise NotImplementedError
    

class FenBoardBuilder(BoardBuilder):
    def __init__(self,  fen: Fen) -> None:
        self._fen = fen
        self._fen_piece_dict = {
            "r": Rook("r"),
            "n": Knight("n"),
            "b": Bishop("b"),
            "q": Queen("q"),
            "k": King("k"),
            "p": Pawn("p"),
            "R": Rook("R"),
            "N": Knight("N"),
            "B": Bishop("B"),
            "Q": Queen("Q"),
            "K": King("K"),
            "P": Pawn("P"),
        }
    

class FenBoardBuilderColumnRow(FenBoardBuilder):
    """Builds a Board by a given Fen """
    def __init__(self,  fen: Fen) -> None:
        super().__init__(fen)
    
    def build_board(self):
        board = []
        row = []
        for character in self._fen._fen_string:
            if character == "/" :
                board.append(row)
                row = []
            elif character.isspace():
                board.append(row)
                break
            elif character in self._fen_piece_dict:
                tile = Tile(self._fen_piece_dict[character])
                row.append(tile)
            elif character.isnumeric():
                for i in range(int(character)): 
                    tile = Tile()
                    row.append(tile)
            else:
                raise InvalidFenNotation
        return board

    def get_iterator(self):
        return BoardIteratorColumnRow(self.build_board())

class FenBoardBuilderOneMatrix(FenBoardBuilder):
    def __init__(self, fen: Fen) -> None:
        super().__init__(fen)
    
    def build_board(self):
        board = []
        for character in self._fen._fen_string:
            if character == "/" :
                continue
            elif character.isspace():
                break
            elif character in self._fen_piece_dict:
                tile = Tile(self._fen_piece_dict[character])
                board.append(tile)
            elif character.isnumeric():
                for i in range(int(character)): 
                    tile = Tile()
                    board.append(tile)
            else:
                raise InvalidFenNotation
        return board
    
    def get_iterator(self):
        return BoardIteratorOneMatrix(self.build_board())

                






