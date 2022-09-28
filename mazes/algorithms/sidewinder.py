from random import choice

from mazes.grids import Grid


class Sidewinder:
    """Generate a maze based on the Binary Tree algorithm.

    The algorithm:
      1. Visit each cell in a row.
      2. For each cell, choose to carve a passage north or east.
      3. If east, carve and move on.
      4. If north, choose a random wall from the run behind and carve.
      3. Move to the next row.
    """

    @staticmethod
    def on(grid: Grid) -> Grid:
        """For each cell of grid, choose at random a northern or
        eastern neighbor to link it to.

        Returns: (Grid)
        """
        for row in grid.each_row():
            run = []

            for cell in row:
                run.append(cell)

                should_close_out = cell.east is None or (
                    cell.north is not None and choice([0, 1]) == 0
                )

                if should_close_out:
                    run_member = choice(run)
                    if run_member.north:
                        run_member.link(run_member.north)
                    run.clear()
                else:
                    cell.link(cell.east)

        return grid
