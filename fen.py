from exceptions.exceptions_fen import InvalidFenNotation, RowLenDiffToRows, ColumnLenDiffToColumns
from piece import Rook, Knight, Bishop, Queen, King, Pawn
class Fen():
    def __init__(self, fen_string: str) -> None:
        self._fen_string = fen_string
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
        self.__filas = 8
        self.__columnas = 8
        if not self.is_fen_valid():
            raise InvalidFenNotation
        
    def _is_character_is_in_possible_dict_pieces(self, character: str):
        return character in self._fen_piece_dict

    
    def get_rows(self):
        rows = []
        current_row = []
        for characther in self._fen_string:
            if characther =="/":
                rows.append(current_row)
                current_row = []
            elif characther.isspace():
                rows.append(current_row)
                break
            else: 
                current_row.append(characther)
        return rows
    
    def count_pieces_in_row(self, row: list[str]):
        piece_counter = 0
        for characther in row:
            if characther.isnumeric():
                piece_counter += int(characther)
            else:
                piece_counter += 1
        return piece_counter

    def is_row_len_equal_to_rows(self):
        return self.__filas == len(self.get_rows())

    def is_column_len_equal_to_columns(self):
        for row in self.get_rows():
            if self.count_pieces_in_row(row) != self.__columnas:
                return False
        return True    

    def is_fen_valid(self):

        if not self.is_row_len_equal_to_rows():
            raise RowLenDiffToRows
        
        if not self.is_column_len_equal_to_columns():
            raise ColumnLenDiffToColumns
        

        
        return True
        
    