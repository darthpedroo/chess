class Coordinates:
    def __init__(self, x_pos, y_pos) -> None:
        self._x_pos = x_pos
        self._y_pos = y_pos
    
    def __eq__(self, other_coordinates: "Coordinates"):
        return (self._x_pos, self._y_pos) == (other_coordinates._x_pos, other_coordinates._y_pos)
    
    def reach_x_threshold(self,threshold: int):
        return self._x_pos == threshold
        
    def increase_x(self,modifier: int):
        self._x_pos += modifier
        
    def increase_y(self, modifier: int):
        self._y_pos += modifier

    def reset_x(self):
        self._x_pos = 0

    def reset_y(self):
        self._y_pos = 0

    def copy(self):
        return Coordinates(self._x_pos, self._y_pos)
    
    def __str__(self) -> str:
        return f"{self._x_pos}{self._y_pos}"