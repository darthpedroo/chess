import pygame
from business.board.i_tile import ITile
from business.board.i_board import IBoard


class BoardDrawer:

    def draw_board(
        self,
        board: IBoard,
        screen,
        tile_size: int,
    ) -> None:

        tile: ITile
        for tile in board:

            row, col = tile.coordinates.get_coordinates()

            pygame.draw.rect(
                screen,
                tile.color,
                pygame.Rect(col * tile_size, row * tile_size, tile_size, tile_size),
            )

            if tile.has_piece():
                center_x = col * tile_size + tile_size // 2
                center_y = row * tile_size + tile_size // 2

                path_to_piece = tile.get_piece().image_path

                piece_image = pygame.image.load(path_to_piece)

                x_scale_refactor = tile_size // 1.5
                y_scale_refactor = tile_size // 1.5

                piece_image = pygame.transform.scale(
                    piece_image, (x_scale_refactor, y_scale_refactor)
                )

                screen.blit(
                    piece_image,
                    (
                        center_x - piece_image.get_width() // 2,
                        center_y - piece_image.get_height() // 2,
                    ),
                )
