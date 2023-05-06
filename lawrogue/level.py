import numpy as np
from numpy.typing import NDArray

from .entity import Entity


class GameMap:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.tiles: NDArray[np.uint8] = np.zeros(
            (width, height), dtype=np.uint8, order="F"
        )
        self.entities: set[Entity] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True is x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height
