from abc import ABC, abstractmethod


class Player(ABC):


    @abstractmethod
    def move_piece(self):
        pass
