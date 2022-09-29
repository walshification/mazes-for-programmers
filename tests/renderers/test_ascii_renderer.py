from textwrap import dedent

from mazes.components import Grid
from mazes.renderers import ASCIIRenderer


def test_ascii_renderer_prints_grid():
    grid = Grid(2, 2)
    renderer = ASCIIRenderer()
    expected = dedent(
        "+---+---+\n" "|   |   |\n" "+---+---+\n" "|   |   |\n" "+---+---+\n"
    )
    assert renderer.render(grid) == expected


def test_ascii_renderer_recognizes_links():
    grid = Grid(2, 2)

    bottom_left = grid[0, 1]
    top_left = grid[0, 0]
    top_right = grid[1, 0]

    bottom_left.link(top_left)
    top_left.link(top_right)

    renderer = ASCIIRenderer()
    expected = dedent(
        "+---+---+\n" "|       |\n" "+   +---+\n" "|   |   |\n" "+---+---+\n"
    )
    assert renderer.render(grid) == expected
