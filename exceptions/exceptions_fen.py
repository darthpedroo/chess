class InvalidFenNotation(Exception):
    def __init__(self) -> None:
        super().__init__("Invalid Fen Notation")

class RowLenDiffToRows(Exception):
    def __init__(self) -> None:
        super().__init__("The number of rows doesn't match the rows from the board")

class ColumnLenDiffToColumns(Exception):
    def __init__(self) -> None:
        super().__init__("The number of columns doesn't match the columns from the board")