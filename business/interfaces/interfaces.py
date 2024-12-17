"""File where general interfaces are located
"""

from abc import ABC, abstractmethod
from business.coordinates.i_coordinates import ICoordinates


class IHaveCoordinates(ABC):
    """Interface for a class that has coordinates"""

    @property
    def coordinates(self) -> ICoordinates:
        """Gets the coordinates"""

    @coordinates.setter
    def coordinates(self, coordinates: ICoordinates):
        """Sets the coordinates"""


class IHaveAPiece(ABC):
    """Interface for classes that have a piece"""

    @abstractmethod
    def has_piece(self) -> bool:
        """Checks if the tile has a piece

        Returns:
            bool: True if it has a piece, false if it does not
        """
