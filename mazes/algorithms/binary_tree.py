from random import choice

from mazes.grids import Grid


class BinaryTree:
    """Generate a maze based on the Binary Tree algorithm.

    The algorithm:
      1. Visit each cell in the grid.
      2. For each cell, choose to carve a passage north or east.
      3. If a cell has an edge, choose the other path.
    """

    @classmethod
    def on(cls, grid: Grid) -> Grid:
        """For each cell of grid, choose at random a northern or
        eastern neighbor to link it to.

        Returns: (Grid)
        """
        grid.algorithm = cls.__name__.lower()
        for cell in grid.each_cell():
            neighbors = [
                neighbor
                for direction in ["north", "east"]
                if (neighbor := getattr(cell, direction))
            ]
            if neighbors:
                cell.link(choice(neighbors))

        return grid
