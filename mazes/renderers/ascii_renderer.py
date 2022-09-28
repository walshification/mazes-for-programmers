from typing import Protocol


class Renderer(Protocol):
    """Protocol definition for renderers."""

    def render(cls, grid) -> str:
        ...


class ASCIIRenderer(Renderer):
    """Renders a maze to the terminal with ASCII art."""

    def render(self, grid) -> str:
        """Draw the grid with ASCII art."""
        output = []
        # Build top row
        output.extend(["+", "---+" * grid.column_length, "\n"])

        for row in grid.each_row():
            corridor = self.build_corridor(row)
            output.append(corridor)

        return "".join(output)

    def build_corridor(self, row) -> str:
        corridor = []
        center = ["|"]  # westernmost wall
        bottom = ["+"]  # westernmost corner

        for cell in row:
            # Add the room space
            center.append("   ")

            if cell.is_linked(cell.east):
                center.append(" ")  # open "door"
            else:
                center.append("|")  # closed wall

            if cell.is_linked(cell.south):
                bottom.append("   ")  # open "door"
            else:
                bottom.append("---")  # closed wall

            bottom.append("+")

        corridor.append("".join(center + ["\n"]))
        corridor.append("".join(bottom + ["\n"]))
        return "".join(corridor)
