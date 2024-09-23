from abc import ABC
from collections.abc import Iterator


class BoardIterator(ABC, Iterator):
    def __init__(self, board_representation) -> None:
        self._board_representation = board_representation
        self._index = 0
    def draw_board(self):
        raise NotImplementedError
    
class BoardIteratorOneMatrix(BoardIterator):
    def __init__(self, board_representation) -> None:
        super().__init__(board_representation)

    def __next__(self):
        if self._index < len(self._board_representation):
            res = self._board_representation[self._index]
            self._index +=1
            return res
        else: 
            raise StopIteration

class BoardIteratorColumnRow(BoardIterator):
    def __init__(self, board_representation) -> None:
        super().__init__(board_representation)
        self._row_index = 0
        self._col_index = 0
    
    def __next__(self):
        if self._row_index < len(self._board_representation):
            row = self._board_representation[self._row_index]
            if self._col_index < len(row):
                tile = row[self._col_index]
                self._col_index += 1
                return tile
            else:
                self._row_index += 1
                self._col_index = 0
                return self.__next__()  # Move to next row
        else:
            raise StopIteration



        