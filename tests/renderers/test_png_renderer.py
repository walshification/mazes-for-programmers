from unittest.mock import call, create_autospec

from PIL import Image, ImageDraw

from mazes.components import Grid
from mazes.renderers import PNGRenderer


def test_png_renderer_draws_a_grid():
    image_class = create_autospec(Image)
    drawing_class = create_autospec(ImageDraw.Draw)
    renderer = PNGRenderer(image_class=image_class, drawing_class=drawing_class)

    renderer.render(Grid(1, 1), filename="some_image")

    image_class.new.assert_called_with("RGBA", (101, 101), (255, 255, 255))
    drawing_class.assert_called_with(image_class.new.return_value)
    drawing_class.return_value.line.assert_has_calls(
        [
            call((0, 0, 100, 0), fill=(0, 0, 0), width=5),
            call((0, 0, 0, 100), fill=(0, 0, 0), width=5),
            call((100, 0, 100, 100), fill=(0, 0, 0), width=5),
            call((0, 100, 100, 100), fill=(0, 0, 0), width=5),
        ]
    )
    image_class.new.return_value.save.assert_called_with(
        "some_image.png", "PNG", optimize=True
    )
