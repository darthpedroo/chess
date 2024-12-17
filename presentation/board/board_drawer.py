import pygame
from business.board.i_tile import ITile
from business.board.i_board import IBoard


class BoardDrawer:
    def draw_board(
        self,
        board: IBoard,
        screen,
        tile_size: int,
        primary_color=(0, 0, 0),
        secondary_color=(255, 255, 255),
    ) -> None:
        tile: ITile
        for tile in board:

            row, col = tile.coordinates.get_coordinates()
            if (row + col) % 2 == 0:
                color = primary_color
            else:
                color = secondary_color

            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size),
            )

            if tile.has_piece():

                # Calculate the center of the tile
                center_x = col * tile_size + tile_size // 2
                center_y = row * tile_size + tile_size // 2

                # Draw the circle at the center of the tile
                pygame.draw.circle(
                    screen, (0, 0, 0), (center_x, center_y), tile_size // 4
                )
