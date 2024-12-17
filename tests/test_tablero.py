from unittest.mock import Mock
import unittest
from business.board.chess_board import ChessBoard
from business.coordinates.coordinates import Coordinates


class TestBoard(unittest.TestCase):

    def setUp(self):
        """Set up a fresh ChessBoard before each test."""
        self.chess_board = ChessBoard()

    def tearDown(self):
        """Clean up resources (if needed) after each test."""
        del self.chess_board

    def test_01_create_board(self):
        chess_board = ChessBoard()
        length_of_board = len(chess_board)
        estimated_length = 8
        self.assertEqual(length_of_board, estimated_length)

    def test_02_tile_has_no_piece(self):
        coords = Coordinates(0, 0)
        tile = self.chess_board.get_tile(coords)
        self.assertFalse(tile.has_piece())

    def test_03_tile_has_piece(self):
        coords = Coordinates(0, 0)
        piece = Mock()
        self.chess_board.add_piece(coords, piece)
        tile = self.chess_board.get_tile(coords)
        self.assertTrue(tile.has_piece())


if __name__ == "__main__":
    unittest.main()
