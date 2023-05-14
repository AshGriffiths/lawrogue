import numpy as np


# Graphic type, compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes for RGB colours.
        ("bg", "3B"),
    ]
)

# Tile type, used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", bool),  # True if tile can be walked over.
        ("transparent", bool),  # True if tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphic for when tile is not in FOV.
    ]
)


def new_tile(
    *,  # Force keyword usage, so parameter order is irrelevant.
    walkable: int,
    transparent: int,
    dark: tuple[int, tuple[int, int, int], tuple[int, int, int]],
) -> np.ndarray:
    """
    Helper function for defining individual tile types.
    """
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (150, 150, 150))
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("█"), (255, 255, 255), (50, 50, 50))
)
