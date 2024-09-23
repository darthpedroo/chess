import unittest
from board import Board
from fen import Fen
from fen_board_builder import FenBoardBuilderColumnRow, FenBoardBuilderOneMatrix
from board_drawer import BoardIteratorOneMatrix

class TestReserva(unittest.TestCase):

    def setUp(self):
        self.fen = Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
       # self.fen_board_builder_column_row = FenBoardBuilderColumnRow(self.fen)
        self.fen_board_builder_one_matrix = FenBoardBuilderColumnRow(self.fen)
        self.board = Board(self.fen_board_builder_one_matrix)
        
    def test_01_iterar_tablero(self):
        for x in self.board:
            print(x)
            print("\n")



    
if __name__ == "__main__":
    unittest.main()