from typing import Protocol


class Renderer(Protocol):
    """Protocol definition for renderers."""

    def render(cls, grid) -> str:
        ...


class ASCIIRenderer(Renderer):
    """Renders a maze to the terminal with ASCII art."""

    def render(cls, grid) -> str:
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
