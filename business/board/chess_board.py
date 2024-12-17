"""Implementation of a chess board
"""

from typing import Iterator
from business.board.i_board import IBoard
from business.board.i_tile import ITile
from business.board.chess_tile import ChessTile
from business.pieces.piece import Piece
from business.coordinates.i_coordinates import ICoordinates
from business.coordinates.coordinates import Coordinates
from business.player.player import Player


class ChessBoard(IBoard):
    def __init__(self, rows=8, columns=8):
        super().__init__(
            rows, columns
        )  # Call parent class __init__ to initialize _rows, _columns, and _board
        self.__board = (
            self._create_empty_board()
        )  # You don't need to reinitialize _rows and _columns here

    def __iter__(self) -> Iterator[ITile]:
        """Iterator to loop through the tiles of the board."""
        for row in self.__board:
            for tile in row:
                yield tile

    def __len__(self) -> tuple[int, int]:
        return len(self.__board)

    def _create_empty_board(self) -> list[list[ITile]]:
        board = []
        for row in range(self._rows):
            board.append([])
            for col in range(self._columns):
                coordinates = Coordinates(row, col)
                new_tile = ChessTile(coordinates)
                board[row].append(new_tile)
        return board

    # def __add_normal_pieces_layout(self):
    #     pass

    def add_piece(self, coordinates: ICoordinates, piece: Piece):
        x, y = coordinates.get_coordinates()
        tile = self.get_tile(coordinates)
        tile.add_piece(piece)
        self.__board[x][y] = tile

    def remove_piece(self, coordinates):
        x, y = coordinates.get_coordinates()
        tile = self.get_tile(coordinates)
        tile.remove_piece()
        self.__board[x][y] = tile

    def get_tile(self, coordinates: ICoordinates) -> ITile:
        x, y = coordinates.get_coordinates()
        tile = self.__board[x][y]
        return tile

    def move_piece(
        self,
        player: Player,
        start_coordinates: ICoordinates,
        end_coordinates: ICoordinates,
    ):

        start_tile = self.get_tile(start_coordinates)

        if not start_tile.has_piece():
            raise ValueError("La tile seleccionada no tiene pieza. Selecciona otra.")

        start_piece = start_tile.get_piece()

        end_tile = self.get_tile(end_coordinates)

        start_tile.remove_piece()
        end_tile.add_piece(start_piece)
