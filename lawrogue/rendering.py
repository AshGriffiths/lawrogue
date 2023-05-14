import numpy as np

from tcod import Console
from tcod.console import rgb_graphic

from .level import GameMap


tile_graphics: np.array = np.array(
    [
        (ord("#"), (0x80, 0x80, 0x80), (0x40, 0x40, 0x40)),  # wall
        (ord("."), (0x40, 0x40, 0x40), (0x18, 0x18, 0x18)),  # floor
    ],
    dtype=rgb_graphic,
)


def render_map(console: Console, game_map: GameMap) -> None:
    console.rgb[0: game_map.width, 0: game_map.height] = tile_graphics[game_map.tiles]

    for entity in game_map.entities:
        console.print(entity.x, entity.y, entity.char, fg=entity.colour)
