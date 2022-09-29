from mazes.algorithms import Sidewinder
from mazes.components import Grid


def test_applies_algortihm_to_each_cell():
    grid = Sidewinder.on(Grid(2, 2))
    assert all(len(cell.links) > 0 for cell in grid.each_cell())
