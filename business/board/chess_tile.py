"""Implementation of a tile for a chess board
"""

from business.board.i_tile import ITile
from business.movement_patterns.movement_patterns import MovementPattern


class ChessTile(ITile):

    def get_possible_moves(self):
        movs = []
        if self.has_piece():

            mov_list: MovementPattern
            for mov_list in self._piece.movement_patterns:
                movs.append(mov_list.get_posible_movements())
            return movs

        return []
