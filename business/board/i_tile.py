"""Tile file
"""

from abc import abstractmethod
from business.interfaces.interfaces import IHaveCoordinates, IHaveAPiece
from business.coordinates.i_coordinates import ICoordinates
from business.pieces.piece import Piece


class ITile(IHaveCoordinates, IHaveAPiece):

    def __init__(self, coordinates: ICoordinates, piece: Piece = None):
        self.__coordinates = coordinates
        self._piece = piece
        self.color = self.__determine_piece_color()

        self.__alternate_color = (255, 0, 255)

    @abstractmethod
    def get_possible_moves(self):
        """Get possible moves of the piece in that tile"""

    def change_to_alternate_color(self):
        self.color = self.__alternate_color

    def reset_color(self):
        self.color = self.__determine_piece_color()

    def __determine_piece_color(self):
        primary_color = (255, 255, 255)
        secondary_color = (0, 0, 0)

        row, col = self.coordinates.get_coordinates()
        if (row + col) % 2 == 0:
            color = primary_color
        else:
            color = secondary_color
        return color

    @property
    def coordinates(self) -> ICoordinates:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates) -> ICoordinates:
        self.__coordinates = coordinates

    def add_piece(self, piece: Piece):
        self._piece = piece

    def get_piece(self) -> Piece:
        return self._piece

    def remove_piece(self):
        self._piece = None

    def has_piece(self):
        return self._piece is not None
