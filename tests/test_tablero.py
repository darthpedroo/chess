from unittest.mock import Mock
import unittest
from business.board.chess_board import ChessBoard
from business.coordinates.coordinates import Coordinates
from business.pieces.piece_factory import PieceFactory


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
        self.chess_board.remove_piece(coords)
        self.assertFalse(tile.has_piece())

    def test_03_tile_has_piece(self):
        coords = Coordinates(0, 0)
        piece = Mock()
        self.chess_board.add_piece(coords, piece)
        tile = self.chess_board.get_tile(coords)
        self.assertTrue(tile.has_piece())

    def test_04_move_piece(self):

        mock_player = Mock()
        piece = PieceFactory().create_piece("queen", "black")
        start_coordinates = Coordinates(4, 4)
        end_coordinates = Coordinates(4, 5)
        self.chess_board.add_piece(start_coordinates, piece)
        self.chess_board.move_piece(mock_player, start_coordinates, end_coordinates)

        self.assertFalse(self.chess_board.get_tile(start_coordinates).has_piece())
        self.assertTrue(self.chess_board.get_tile(end_coordinates).has_piece())

    def test_05_move_piece_where_there_is_no_piece_raises_error(self):
        start_coordinates = Coordinates(1, 3)
        end_coordinates = Coordinates(1, 4)
        player = Mock()
        with self.assertRaises(ValueError):
            self.chess_board.move_piece(player, start_coordinates, end_coordinates)


if __name__ == "__main__":
    unittest.main()
