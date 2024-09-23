from coordinates import Coordinates
from board import Board

class Player:
    def __init__(self) -> None:
        pass

    def move_piece(self, board: Board,  initial_coordinates: Coordinates, final_coordinates: Coordinates):
        return board.move_piece(initial_coordinates,final_coordinates)
    
        