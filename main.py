import random
import pygame
from business.board.chess_board import ChessBoard
from business.pieces.piece_factory import PieceFactory
from business.coordinates.coordinates import Coordinates
from presentation.board.board_drawer import BoardDrawer

from presentation.colors import *  # pylint: disable = W0401 W0614


# Initialize Pygame
pygame.init()  # pylint: disable = E1101

# Set up screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chessboard")


# Define the size of the grid
GRID_SIZE = 8
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE  # Dividing screen width into 8 tiles


# Function to draw a chessboard
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            # Alternate colors for the tiles
            if (row + col) % 2 == 0:
                color = WHITE  # White tile
            else:
                color = BLACK  # Black tile
            # Draw the rectangle (tile)
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE),
            )


def main():
    running = True

    primary = random.choice(COLORS)
    COLORS.remove(primary)
    secondary = random.choice(COLORS)

    PRIMARY_COLOR = primary
    SECONDARY_COLOR = secondary

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pylint: disable = E1101
                running = False

        screen.fill(GREEN)

        chess_board = ChessBoard()

        coords = Coordinates(0, 0)
        piece_factory = PieceFactory()

        pawn = piece_factory.create_piece("pawn", "black")

        chess_board.add_piece(coords, pawn)
        board_drawer = BoardDrawer()

        board_drawer.draw_board(
            chess_board, screen, TILE_SIZE, PRIMARY_COLOR, SECONDARY_COLOR
        )
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()  # pylint: disable = E1101


if __name__ == "__main__":
    main()
