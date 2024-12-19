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
from business.pieces.piece_factory import PieceFactory


class ChessBoard(IBoard):
    def __init__(self, rows=8, columns=8):
        super().__init__(rows, columns)
        self.__board = self._create_empty_board()
        self.__add_normal_pieces_layout()

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

    def __add_normal_pieces_layout(self):

        piece_factory = PieceFactory()

        for col in range(self._columns):

            black_pawn_coords = Coordinates(1, col)
            white_pawn_coords = Coordinates(6, col)
            black_pawn = piece_factory.create_piece("pawn", "black")
            white_pawn = piece_factory.create_piece("pawn", "white")
            self.add_piece(black_pawn_coords, black_pawn)
            self.add_piece(white_pawn_coords, white_pawn)

        # Rooks
        black_rook = piece_factory.create_piece("rook", "black")
        white_rook = piece_factory.create_piece("rook", "white")

        self.add_piece(Coordinates(0, 0), black_rook)
        self.add_piece(Coordinates(0, 7), black_rook)
        self.add_piece(Coordinates(7, 0), white_rook)
        self.add_piece(Coordinates(7, 7), white_rook)

        # Knights
        black_knight = piece_factory.create_piece("knight", "black")
        white_knight = piece_factory.create_piece("knight", "white")

        self.add_piece(Coordinates(0, 1), black_knight)
        self.add_piece(Coordinates(0, 6), black_knight)
        self.add_piece(Coordinates(7, 1), white_knight)
        self.add_piece(Coordinates(7, 6), white_knight)

        # Bishops
        black_bishop = piece_factory.create_piece("bishop", "black")
        white_bishop = piece_factory.create_piece("bishop", "white")

        self.add_piece(Coordinates(0, 2), black_bishop)
        self.add_piece(Coordinates(0, 5), black_bishop)
        self.add_piece(Coordinates(7, 2), white_bishop)
        self.add_piece(Coordinates(7, 5), white_bishop)

        # Queens
        black_queen = piece_factory.create_piece("queen", "black")
        white_queen = piece_factory.create_piece("queen", "white")

        self.add_piece(Coordinates(0, 3), black_queen)
        self.add_piece(Coordinates(7, 3), white_queen)

        # King
        black_king = piece_factory.create_piece("king", "black")
        white_king = piece_factory.create_piece("king", "white")

        self.add_piece(Coordinates(0, 4), black_king)
        self.add_piece(Coordinates(7, 4), white_king)

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

    def change_tile_color(self, coordinates, color):
        tile = self.get_tile(coordinates)
        tile.change_to_alternate_color()
        x, y = coordinates.get_coordinates()
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

        possible_movs = start_tile.get_possible_moves()

        if not start_tile.has_piece():
            raise ValueError("La tile seleccionada no tiene pieza. Selecciona otra.")

        start_piece = start_tile.get_piece()

        end_tile = self.get_tile(end_coordinates)

        temp_movs = self.check_path(start_coordinates, possible_movs)

        if end_coordinates in temp_movs:
            start_tile.remove_piece()
            end_tile.add_piece(start_piece)
        else:
            raise ValueError("No se puede mover eso mijo")

    # Esto podria ir en partida ???
    def check_path(self, start_coordinates: Coordinates, possible_movs):
        temp_movs = []

        for mov in possible_movs:
            for coordinate in mov:
                temp = start_coordinates + coordinate
                try:
                    tile = self.get_tile(temp)
                    start_piece = self.get_tile(start_coordinates).get_piece()

                    has_piece = tile.has_piece()
                    is_opponent = (
                        has_piece and tile.get_piece().color != start_piece.color
                    )

                    if has_piece:
                        if is_opponent:
                            temp_movs.append(temp)
                        break

                    temp_movs.append(temp)

                except IndexError:
                    pass  # Ignore out-of-bounds coordinates

        return temp_movs
