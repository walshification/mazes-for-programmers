from mazes.grid import Cell


def test_cell_position():
    cell = Cell(2, 3)
    assert (cell.row, cell.column) == (2, 3)


def test_cell_can_link():
    cell = Cell(0, 0)
    other = Cell(1, 0)

    cell.link(other)

    assert cell.is_linked(other) is True
    assert other.is_linked(cell) is True


def test_cell_returns_links():
    cell = Cell(0, 0)
    other = Cell(1, 0)

    cell.link(other)

    assert cell.links == [other]


def test_cell_can_unlink():
    cell = Cell(0, 0)
    other = Cell(1, 0)

    cell.link(other)
    cell.unlink(other)

    assert cell.is_linked(other) is False
    assert other.is_linked(cell) is False


def test_cell_returns_neighbors():
    cell = Cell(1, 1)
    north = Cell(1, 2)
    south = Cell(1, 0)
    east = Cell(2, 1)
    west = Cell(0, 1)

    cell.north = north
    cell.south = south
    cell.east = east
    cell.west = west

    assert cell.neighbors == [north, south, east, west]


def test_cell_skips_empty_neighbors():
    cell = Cell(1, 1)
    north = Cell(1, 2)
    east = Cell(2, 1)
    west = Cell(0, 1)

    cell.north = north
    # no south
    cell.east = east
    cell.west = west

    assert cell.neighbors == [north, east, west]
