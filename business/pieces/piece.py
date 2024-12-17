from abc import ABC


class Piece(ABC):

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    @property
    def image_path(self):
        return f"assets/{self.color}_{self.name}.png"
