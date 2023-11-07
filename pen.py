from typing import Tuple
import math

from PIL import Image, ImageDraw


class Pen:
    def __init__(
        self, image_dimensions: Tuple[int, int], pen_pos: Tuple = (0, 0), width: int = 0, colour: str="#EC99B2"
    ):
        self.pos = pen_pos
        self.heading = 0.0
        self.is_down = False
        self.bg = "#4C4C4C"
        self.colour = colour
        self.canvas_size = image_dimensions
        self.image = Image.new("RGBA", self.canvas_size, self.bg)
        self.drawing = ImageDraw.Draw(self.image)
        self.width = width

    def forward(self, dist: float):
        newpos = (
            (dist * math.cos(self.heading)) + self.pos[0],
            (dist * math.sin(self.heading)) + self.pos[1],
        )
        if self.is_down:
            self.drawing.line(self.pos + newpos, fill=self.colour, width=self.width)
        self.pos = newpos

    def left(self, heading: float):
        radians = (heading * math.pi) / 180.0
        self.heading -= radians

    def right(self, heading: float):
        radians = (heading * math.pi) / 180.0
        self.heading += radians

    def up(self):
        self.is_down = False

    def down(self):
        self.is_down = True

    def set_pos(self, newpos: Tuple):
        self.pos = newpos

    def set_width(self, new_width: int):
        self.width = new_width

    def set_heading(self, new_heading: float):
        radians = (new_heading * math.pi) / 180.0
        self.heading = radians

    def get_pos(self) -> Tuple:
        return self.pos

    def get_heading(self) -> float:
        degrees = (self.heading * 180) / math.pi
        return degrees

    def set_colour(self, new_colour: str):
        self.colour = new_colour

    def set_bg(self, new_bg: str):
        self.bg = new_bg

    def set_canvas_size(self, size: Tuple[int, int]):
        self.canvas_size = size
        self.image = Image.new("RGBA", self.canvas_size, self.bg)
        self.drawing = ImageDraw.Draw(self.image)

    def show(self):
        self.image.show()

    def save(self, filename):
        self.image.save(filename, "PNG")

    def get_image(self) -> Image.Image:
        return self.image
