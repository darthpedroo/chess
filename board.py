from typing import Iterator
from fen import Fen
from fen_board_builder import BoardBuilder
from board_drawer import BoardIterator
from collections.abc import Iterable


class Board(Iterable):
    def __init__(self, board_builder: BoardBuilder) -> None:
        self._board_builder = board_builder
        self._board_representation = board_builder.build_board()
    
    def __iter__(self) -> Iterator:
        iterator = self._board_builder.get_iterator()
        return iterator
