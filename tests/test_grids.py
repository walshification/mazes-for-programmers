from mazes.cells import Cell
from mazes.grids import Grid


def test_grid_creates_itself():
    grid = Grid(2, 3)
    assert grid.row_length == 2
    assert grid.column_length == 3
    assert len(grid) == 6


def test_grid_is_made_of_cells():
    grid = Grid(1, 2)
    assert list(str(cell) for cell in grid.each_cell()) == ["(0, 0)", "(0, 1)"]


def test_grid_allows_random_access():
    grid = Grid(3, 3)
    cell = grid.random_cell()
    assert cell in grid


def test_grid_knows_its_own_cells():
    grid = Grid(1, 1)
    assert not Cell(0, 0) in grid
