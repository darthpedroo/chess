from abc import ABC
from business.movement_patterns.movement_patterns import MovementPattern


class Piece(ABC):

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.movement_patterns: MovementPattern
        self.movement_patterns = []

    @property
    def image_path(self):
        return f"assets/{self.color}_{self.name}.png"
