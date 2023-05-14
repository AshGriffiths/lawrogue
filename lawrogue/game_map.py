import numpy as np

from tcod.console import Console

from . import tile_types


class GameMap:
    def __init__(self, width: int, height: int) -> None:
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

        self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True is x and y are inside of the bounds of this map
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0 : self.width, 0 : self.height] = self.tiles["dark"]