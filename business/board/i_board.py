"""Interface for the board
"""

from abc import ABC, abstractmethod
from business.coordinates.i_coordinates import ICoordinates
from business.board.i_tile import ITile
from business.pieces.piece import Piece
from business.player.player import Player


class IBoard(ABC):
    def __init__(self, rows: int = 8, columns: int = 8):
        self._rows = rows
        self._columns = columns

    def __iter__(self) -> ITile:
        """Iters through the board"""

    @abstractmethod
    def _create_empty_board(self) -> list[list[ITile]]:
        """Creates an empty board

        Returns:
            list[list[ITile]]: the representation of the board
        """

    @abstractmethod
    def add_piece(self, coordinates: ICoordinates, piece: Piece):
        """Adds a piece to the board coordinates

        Args:
            coordinates (ICoordinates): Coordinates to add the pieces
            piece (Piece): Piece to add to that coordinate
        """

    @abstractmethod
    def remove_piece(self, coordinates: ICoordinates):
        """Removes a piece from the boad

        Args:
            coordinates (ICoordinates): Coordinate to remove the piece
        """

    @abstractmethod
    def move_piece(
        self,
        player: Player,
        start_coordinates: ICoordinates,
        end_coordinates: ICoordinates,
    ):
        """Moves a piece from coordinates A to coordinates B

        Args:
            start_coordinates (ICoordinates): Starting position of the piece
            end_coordinates (ICoordinates): End position (desired position) of the coordinate
        """

    @abstractmethod
    def get_tile(self, coordinates: ICoordinates) -> ITile:
        """Gets the tile based on the coordinates

        Args:
            coordinates (ICoordinates):

        Returns:
            ITile:
        """
    
    @abstractmethod
    def change_tile_color(self, coords:ICoordinates,color:tuple[int,int,int]):
        """Changes the color of a tile

        Args:
            color (tuple[int,int,int]): Desired color
        """
    