import pygame
from business.coordinates.coordinates import Coordinates
from business.board.i_board import IBoard

class InputHandler():
    
    
    def get_mouse_position(self):
        return pygame.mouse.get_pos()
    
    def get_coordinates_from_mouse_position(self, tile_size:int) -> Coordinates:
        x , y = self.get_mouse_position()
        col = x // tile_size
        row = y // tile_size
        return Coordinates(row,col)
    
    def change_color_on_click(self, board:IBoard, tile_size:int):
        
        coords = self.get_coordinates_from_mouse_position(tile_size)
        board.change_tile_color(coords, (0,255,0))
    
    def move_piece(self, chess_board:IBoard, player, last_clicked_tile_coordinates:Coordinates, tile_size: int):
        
        player = "Stub!"

        if last_clicked_tile_coordinates is not None:
            chess_board.get_tile(last_clicked_tile_coordinates).reset_color()


        start_cordinates = self.get_coordinates_from_mouse_position(tile_size)
        self.change_color_on_click(chess_board, tile_size)
        
        return start_cordinates
                
        
        
        