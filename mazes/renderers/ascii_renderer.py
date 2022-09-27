from typing_extensions import Protocol

from mazes.cells import Cell
# from mazes.grids import Grid


class Renderer(Protocol):
    """Protocol definition for renderers."""

    @classmethod
    def render(cls, grid: "Grid") -> str:
        ...



class ASCIIRenderer:
    """Renders a maze to the terminal with ASCII art."""

    @classmethod
    def render(cls, grid: "Grid") -> str:
        """Draw the grid with ASCII art."""
        output = []
        # Build top row
        output.extend(["+", "---+" * grid.column_length, "\n"])

        for row in grid.each_row():
            corridor = ["|"]  # westernmost wall
            bottom = ["+"]  # westernmost corner

            for cell in row:
                # Add the room space
                corridor.append("   ")

                if cell.is_linked(cell.east):
                    corridor.append(" ")  # open "door"
                else:
                    corridor.append("|")  # closed wall

                if cell.is_linked(cell.south):
                    bottom.append("   ")  # open "door"
                else:
                    bottom.append("---")  # closed wall

                bottom.append("+")

            output.extend(["".join(corridor), "\n"])
            output.extend(["".join(bottom), "\n"])

        return "".join(output)
