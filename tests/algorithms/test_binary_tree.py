from mazes.algorithms import BinaryTree
from mazes.grids import Grid


def test_applies_algortihm_to_each_cell():
    grid = BinaryTree.on(Grid(2, 2))
    assert all(len(cell.links) > 0 for cell in grid.each_cell())
