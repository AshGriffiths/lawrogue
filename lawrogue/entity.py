class Entity:
    """A generic object to represent entities in the world, such as players, enemies, items and so-on."""

    def __init__(
        self,
        x: int,
        y: int,
        char: str,
        colour: tuple[int, int, int],
    ) -> None:
        self.x: int = x
        self.y: int = y
        self.char: str = char
        self.colour: tuple[int, int, int] = colour
