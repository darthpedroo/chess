import logging
import pygame
from business.board.chess_board import ChessBoard
from presentation.board.board_drawer import BoardDrawer
from presentation.inputs.input_handler import InputHandler

from presentation.colors import *  # pylint: disable = W0401 W0614


# Initialize Pygame
pygame.init()  # pylint: disable = E1101

# Set up screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CHESS")


def main():
    running = True
    input_handler = InputHandler()
    chess_board = ChessBoard()

    selected_tile_coordinates = None
    TILE_SIZE = SCREEN_WIDTH // len(chess_board)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable = E1101
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable = E1101
                if event.button == 1:  # Left mouse button

                    clicked_coordinates = (
                        input_handler.get_coordinates_from_mouse_position(TILE_SIZE)
                    )
                    clicked_tile = chess_board.get_tile(clicked_coordinates)

                    if selected_tile_coordinates:
                        try:
                            chess_board.move_piece(
                                "Player Stub",
                                selected_tile_coordinates,
                                clicked_coordinates,
                            )
                        except ValueError:
                            pass

                        chess_board.get_tile(selected_tile_coordinates).reset_color()
                        selected_tile_coordinates = None
                    else:
                        selected_tile_coordinates = clicked_coordinates
                        clicked_tile.change_to_alternate_color()

                elif event.button == 3:
                    if selected_tile_coordinates is not None:
                        chess_board.get_tile(selected_tile_coordinates).reset_color()
                        selected_tile_coordinates = None

        board_drawer = BoardDrawer()
        board_drawer.draw_board(chess_board, screen, TILE_SIZE)

        pygame.display.flip()

    pygame.quit()  # pylint: disable = E1101


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,  # Set logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",  # Log message format
    )
    main()
