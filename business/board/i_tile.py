"""Tile file
"""

from business.interfaces.interfaces import IHaveCoordinates, IHaveAPiece
from business.coordinates.i_coordinates import ICoordinates
from business.pieces.piece import Piece


class ITile(IHaveCoordinates, IHaveAPiece):

    def __init__(self, coordinates: ICoordinates, piece: Piece = None):
        self.__coordinates = coordinates
        self.__piece = piece

    @property
    def coordinates(self) -> ICoordinates:
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates) -> ICoordinates:
        self.__coordinates = coordinates

    def add_piece(self, piece: Piece):
        self.__piece = piece

    def get_piece(self) -> Piece:
        return self.__piece

    def remove_piece(self):
        self.__piece = None

    def has_piece(self):
        return self.__piece is not None
