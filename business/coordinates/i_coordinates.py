from abc import ABC, abstractmethod


class ICoordinates(ABC):

    @abstractmethod
    def get_coordinates(self):
        pass
