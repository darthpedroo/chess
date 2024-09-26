from piece import Piece
from coordinates import Coordinates
from exceptions.exceptions import TileHasPiece

class Tile():
    def __init__(self, coordinates: Coordinates,piece:Piece=None,) -> None:
        self._coordinates = coordinates
        self._piece = piece
    
    def __eq__(self, other_tile: "Tile") -> bool:
        return (self._coordinates) == (other_tile._coordinates)

    def has_piece(self):
        return self._piece != None

    def are_coordinates_equal(self, coordinates: Coordinates):
        return self._coordinates == coordinates
    
    def display_tile(self):
        if self.has_piece():
            return f" {self._piece.display_piece()} "
        else:
            return f" - "
    
    def pop_piece(self):
        old_piece = self._piece
        self._piece = None
        return old_piece

    def set_piece(self, new_piece: Piece):
        if self._piece is not None:
            raise TileHasPiece
        self._piece = new_piece
        
