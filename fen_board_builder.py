from abc import ABC
from fen import Fen
from tile import Tile
from piece import Rook, Knight, Bishop, Queen, King, Pawn
from exceptions.exceptions_fen import InvalidFenNotation

from collections.abc import Iterator
from board_iterator import BoardIteratorOneMatrix, BoardIteratorColumnRow
from coordinates import Coordinates


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
    
    def change_coordinates(self, coordinates: Coordinates):
        newcords = coordinates.copy()
        if newcords.reach_x_threshold(7):
            newcords.reset_x()
            newcords.increase_y(1)
        else:
            newcords.increase_x(1)    
        return newcords
    
class FenBoardBuilderOneMatrix(FenBoardBuilder):
    def __init__(self, fen: Fen) -> None:
        super().__init__(fen)
    
    def build_board(self): #Pasar acá el FEN
        coordinates = Coordinates(0,0)
        board = []
        for character in self._fen._fen_string:
            if character == "/" :
                continue
            elif character.isspace():
                break
            elif character in self._fen_piece_dict:
                tile = Tile(coordinates, self._fen_piece_dict[character])
                board.append(tile)
                coordinates = self.change_coordinates(coordinates)
            elif character.isnumeric():
                for i in range(int(character)):
                    tile = Tile(coordinates)
                    board.append(tile)
                    coordinates = self.change_coordinates(coordinates)
            else:
                raise InvalidFenNotation
            

        return board
    
    def get_iterator(self):
        return BoardIteratorOneMatrix(self.build_board())

                






