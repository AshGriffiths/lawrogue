import pytest

from lawrogue.entity import Entity


@pytest.fixture
def player() -> Entity:
    return Entity(1, 1, "@", (255, 255, 255))


class TestEntity:
    def test_creation(self, player: Entity):
        assert player.x == 1
        assert player.y == 1
        assert player.char == "@"
        assert player.color == (255, 255, 255)

    def test_move(self, player: Entity):
        player.move(1, 0)
        assert player.x == 2
        assert player.y == 1
        player.move(-1, 0)
        assert player.x == 1
        assert player.y == 1
        player.move(0, 1)
        assert player.x == 1
        assert player.y == 2
        player.move(0, -1)
        assert player.x == 1
        assert player.y == 1
