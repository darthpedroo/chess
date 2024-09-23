class InvalidFenNotation(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid Fen Notation")
