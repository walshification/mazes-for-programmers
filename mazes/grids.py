from random import choice
from typing import Iterator, List, Optional, Tuple

from mazes.cells import Cell


class Grid:
    """A 2-dimensional list of cells.

    Attributes:
      row_length (int): the number of cells making up the x-axis.
      column_length (int): the number of cells making up the y-axis.
    """

    def __init__(self, row_length: int, column_length: int) -> None:
        self.row_length = row_length
        self.column_length = column_length
        self._grid = self._prepare_grid()
        self._configure_cells()

    def __contains__(self, cell: Cell) -> bool:
        """Return whether cell is found in grid or not."""
        return any(cell == grid_cell for grid_cell in self.each_cell())

    def __len__(self) -> int:
        """Return number of cells in grid."""
        return self.row_length * self.column_length

    def __getitem__(self, position: Tuple[int, int]) -> Optional[Cell]:
        """Return cell found at (row, column) or None."""
        row, column = position

        if row < 0 or row >= self.row_length:
            return None

        if column < 0 or column >= self.column_length:
            return None

        return self._grid[row][column]

    def each_row(self) -> Iterator[List[Cell]]:
        """Return each row of the grid."""
        return (row for row in self._grid)

    def each_cell(self) -> Iterator[Cell]:
        """Return each cell of the grid."""
        return (cell for row in self.each_row() for cell in row)

    def random_cell(self) -> Cell:
        """Return a random cell in the grid."""
        row = choice(range(self.row_length))
        column = choice(range(self.column_length))
        return self._grid[row][column]

    def _prepare_grid(self) -> List[List[Cell]]:
        """Return a 2-dimensional list of cells."""
        return [
            [Cell(row, column) for column in range(self.column_length)]
            for row in range(self.row_length)
        ]

    def _configure_cells(self) -> None:
        """Assign each cell its immediate neighbors."""
        for cell in self.each_cell():
            row, column = cell

            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.east = self[row, column + 1]
            cell.west = self[row, column - 1]
