from abc import ABC


class Piece(ABC):

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
