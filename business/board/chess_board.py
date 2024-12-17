"""Implementation of a chess board
"""

from business.board.i_board import IBoard
from business.board.i_tile import ITile
from business.board.chess_tile import ChessTile
from business.pieces.piece import Piece
from business.coordinates.i_coordinates import ICoordinates
from business.coordinates.coordinates import Coordinates


class ChessBoard(IBoard):
    def __init__(self, rows=8, columns=8):
        super().__init__(rows, columns)  # Call parent class __init__ to initialize _rows, _columns, and _board
        self.__board = self._create_empty_board()  # You don't need to reinitialize _rows and _columns here


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
        pass

    def get_tile(self, coordinates: ICoordinates) -> ITile:
        x, y = coordinates.get_coordinates()
        tile = self.__board[x][y]
        return tile

    def move_piece(self, player, start_coordinates, end_coordinates):
        pass
