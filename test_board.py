import unittest
from board import Board
from fen import Fen
from fen_board_builder import FenBoardBuilderOneMatrix
from game_processor import GameProcessorConsole
from player import Player
from tile import Tile
from coordinates import Coordinates




class TestBoard(unittest.TestCase):

    def setUp(self):
        self.fen = Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.fen_board_builder_one_matrix = FenBoardBuilderOneMatrix(self.fen)
        self.board = Board(self.fen_board_builder_one_matrix)
        self.game_processor_console = GameProcessorConsole()
        
    def test_01_iterar_tablero(self):
        self.game_processor_console.draw_board(self.board)
    
    def test_02_jugador_mueve_pieza_tablero(self):
        print("New Board")
        porky = Player()
        new_board = porky.move_piece(self.board, Coordinates(0, 0), Coordinates(4, 4))
        self.game_processor_console.draw_board(new_board)  

    def test_03_jugador_mueve_pieza_tablero_que_no_es_suya(self):
        pass

if __name__ == "__main__":
    unittest.main()

