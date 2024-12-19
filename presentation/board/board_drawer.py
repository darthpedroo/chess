import pygame
from business.board.i_tile import ITile
from business.board.i_board import IBoard
from business.board.chess_board import ChessBoard
from business.coordinates.coordinates import Coordinates
from presentation.colors import RED, GRAY


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

    def draw_dot_for_move(
        self,
        screen,
        row: int,
        col: int,
        tile_size: int,
        color,
        radius: int,
        thickness: int,
    ):
        center_x = col * tile_size + tile_size // 2
        center_y = row * tile_size + tile_size // 2
        pygame.draw.circle(screen, color, (center_x, center_y), radius, thickness)

    def draw_possible_moves(
        self, board: ChessBoard, start_coordinates: Coordinates, screen, tile_size: int
    ):
        tile = board.get_tile(start_coordinates)
        movs = tile.get_possible_moves()
        final_possible_moves = board.check_path(start_coordinates, movs)

        for coordinates in final_possible_moves:
            row, col = coordinates.get_coordinates()
            other_tile = board.get_tile(coordinates)

            has_piece = other_tile.has_piece()
            is_enemy = (
                has_piece and other_tile.get_piece().color != tile.get_piece().color
            )

            if is_enemy:
                color = RED
                radius = tile_size // 2
                thickness = 5
            else:
                color = GRAY
                radius = tile_size // 6
                thickness = 0

            self.draw_dot_for_move(
                screen, row, col, tile_size, color, radius, thickness
            )
