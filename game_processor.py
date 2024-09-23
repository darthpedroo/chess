from abc import ABC
from board import Board
from tile import Tile

class GameProcessor(ABC):
    def draw_board(self):
        raise NotImplementedError

class GameProcessorConsole(GameProcessor):
    def __init__(self) -> None:
        pass
       # self.__board = board

    def draw_board(self, board):
        index = 0
        for tile in board:
            tile: Tile
            if index % 8 == 0:
                print("\n")  
            print(tile.display_tile(), end="")
            index += 1
        print("\n")  




