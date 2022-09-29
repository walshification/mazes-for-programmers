from datetime import datetime

from PIL import Image, ImageDraw


class PNGRenderer:
    """Convert a maze into a PNG image."""

    def __init__(self, image_class=Image, drawing_class=ImageDraw.Draw) -> None:
        self.image_class = image_class
        self.drawing_class = drawing_class

    def render(self, grid, cell_size: int = 100, filename: str = None) -> None:
        maze_type = f"{grid.algorithm}_" if grid.algorithm is not None else ""
        filename = filename or (
            f"{maze_type}{str(datetime.now().timestamp()).replace('.', '')}"
        )
        image = self.create_png(grid, cell_size)
        image.save(f"{filename}.png", "PNG", optimize=True)

    def create_png(self, grid, cell_size: int) -> Image.Image:
        wall_color = (0, 0, 0)
        image_width = cell_size * grid.column_length
        image_height = cell_size * grid.row_length

        image = self.image_class.new(
            "RGBA", (image_width + 1, image_height + 1), (255, 255, 255)
        )
        draw = self.drawing_class(image)

        for cell in grid.each_cell():
            x1 = cell.column * cell_size
            y1 = cell.row * cell_size
            x2 = (cell.column + 1) * cell_size
            y2 = (cell.row + 1) * cell_size

            if not cell.north:
                draw.line((x1, y1, x2, y1), fill=wall_color, width=5)
            if not cell.west:
                draw.line((x1, y1, x1, y2), fill=wall_color, width=5)
            if not cell.is_linked(cell.east):
                draw.line((x2, y1, x2, y2), fill=wall_color, width=5)
            if not cell.is_linked(cell.south):
                draw.line((x1, y2, x2, y2), fill=wall_color, width=5)

        return image
