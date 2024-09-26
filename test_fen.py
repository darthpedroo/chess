import unittest
from board import Board
from fen import Fen
from exceptions.exceptions_fen import RowLenDiffToRows, ColumnLenDiffToColumns





class TestFen(unittest.TestCase):

    def setUp(self):
        self.fen = Fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

    def test_master_is_fen_valid(self):
        self.assertTrue(self.fen.is_fen_valid())

    def test_01_get_rows_from_fen(self):
        rows = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], ['8'], ['8'], ['8'], ['8'], ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self.assertTrue(self.fen.get_rows() == rows)
    
    def test_02_is_row_len_equal_to_rows_in_board(self):
        self.assertTrue(self.fen.is_row_len_equal_to_rows())
    
    def test_03_row_len_different_to_rows_throws_error(self):
        with self.assertRaises(RowLenDiffToRows):
            fen = Fen("rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            self.assertTrue(fen.is_fen_valid())
    
    def test_04_column_len_different_to_columns_throws_error(self):
        with self.assertRaises(ColumnLenDiffToColumns):
            print("Poop")
            feno = Fen("rnbqkbnr/p9/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            self.assertTrue(feno.is_fen_valid())

    def test_05_column_len_equal_to_columns_in_board(self):
        self.assertTrue(self.fen.is_column_len_equal_to_columns())

    def test_06_every_piece_has_valid_notation(self):
        pass

    def test_07_no_consecutive_numbers_to_represent_empty_spaces(self):
        pass

    

    
            


if __name__ == "__main__":
    unittest.main()

