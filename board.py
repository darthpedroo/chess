from typing import Iterator
from fen import Fen
from fen_board_builder import BoardBuilder
from board_iterator import BoardIterator
from collections.abc import Iterable
from coordinates import Coordinates
from tile import Tile
from exceptions import TileNotFound, TileHasNoPiece, TileHasPiece

class Board(Iterable):
    def __init__(self, board_builder: BoardBuilder) -> None:
        self._board_builder = board_builder
        self._board_representation = board_builder.build_board()
    
    def __iter__(self) -> Iterator:
        iterator = self._board_builder.get_iterator()
        return iterator

    def get_tile_from_coordinates(self, input_coordinates: Coordinates):
        for tile in self._board_representation:
            tile: Tile
            if tile.are_coordinates_equal(input_coordinates):
                return tile
        raise TileNotFound
    
    def change_tile(self, new_tile: Tile):
        for index, tile in enumerate(self._board_representation):
            if tile.are_coordinates_equal(new_tile._coordinates):
                self._board_representation[index] = new_tile  
                break
    
    def change_piece_position(self, initial_tile, final_tile):
        pass

    def move_piece(self, initial_coordinates: Coordinates, final_coordinates: Coordinates):
        initial_tile = self.get_tile_from_coordinates(initial_coordinates)
        final_tile = self.get_tile_from_coordinates(final_coordinates)

        if not initial_tile.has_piece():
            raise TileHasNoPiece
        
        if final_tile.has_piece():
            raise TileHasPiece
        
        piece = initial_tile.pop_piece()
        print(f"Moving {piece}, {initial_tile} from {initial_tile._coordinates} to {final_tile._coordinates}")  # Debugging

        final_tile.set_piece(piece)
        self.change_tile(initial_tile)
        self.change_tile(final_tile)
        print(f"Piece moved. New state at {final_tile._coordinates}: {final_tile}")
        return self._board_representation
        #al mover la pieza se tiene que RECONSTRUIR EL FEN !


        




