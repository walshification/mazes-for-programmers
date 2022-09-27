from typing import Dict, List


class Cell:
    """A node for a grid.

    Attributes:
      row (int): the row (x-axis) of the cell.
      column (int): the column (y-axis) of the cell.
      north (Optional[Cell]): the neighboring cell to the north.
      south (Optional[Cell]): the neighboring cell to the south.
      east (Optional[Cell]): the neighboring cell to the east.
      west (Optional[Cell]): the neighboring cell to the west.
    """

    def __init__(self, row: int, column: int) -> None:
        """Set the cell's position."""
        self.row, self.column = row, column
        self._links: Dict["Cell", bool] = {}
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    @property
    def links(self) -> List["Cell"]:
        """Return a list of cells linked to this one."""
        return list(self._links.keys())

    @property
    def neighbors(self) -> List["Cell"]:
        """Return a list of the cell's neighbors."""
        return [
            neighbor
            for cardinal_direction in ["north", "south", "east", "west"]
            if (neighbor := getattr(self, cardinal_direction))
        ]

    def is_linked(self, other: "Cell") -> bool:
        """Return whether cell is linked to other."""
        return other in self._links

    def link(self, other: "Cell", bidirectional: bool = True) -> None:
        """Establish a link between this cell and another.

        Args:
          other (Cell): the cell to link.
          bidirectional (bool): establishes the link from the other
            direction.
        """
        self._links[other] = True
        if bidirectional:
            other.link(self, False)

    def unlink(self, other: "Cell", bidirectional: bool = True) -> None:
        """Break a link between this cell and another.

        Args:
          other (Cell): the cell to unlink.
          bidirectional (bool): breaks the link from the other
            direction.
        """
        del self._links[other]
        if bidirectional:
            other.unlink(self, False)
