import pytest

from lawrogue.game_map import GameMap


@pytest.fixture
def game_map() -> GameMap:
    return GameMap(60, 20)


class TestGameMap:
    def test_creation(self, game_map: GameMap) -> None:
        assert game_map.width == 60
        assert game_map.height == 20

    def test_in_bounds(self, game_map: GameMap) -> None:
        # Check normal coords
        assert game_map.in_bounds(5, 5) is True
        # Negative x out of bounds
        assert game_map.in_bounds(-1, 5) is False
        # Negative y out of bounds
        assert game_map.in_bounds(5, -1) is False
        # Origin is in bounds
        assert game_map.in_bounds(0, 0) is True
        # Width and height are out of bounds
        assert game_map.in_bounds(game_map.width, game_map.height) is False
        # Width - 1 and height - 1 are in bounds
        assert game_map.in_bounds(game_map.width - 1, game_map.height - 1) is True
