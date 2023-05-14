import copy
import pytest

from lawrogue import entity_factories
from lawrogue.actions import MovementAction
from lawrogue.engine import Engine
from lawrogue.entity import Entity
from lawrogue.game_map import GameMap
from lawrogue.input_handlers import EventHandler
from lawrogue.procgen import generate_dungeon


@pytest.fixture
def move_up() -> MovementAction:
    return MovementAction(0, 1)


@pytest.fixture
def move_down() -> MovementAction:
    return MovementAction(0, -1)


@pytest.fixture
def move_left() -> MovementAction:
    return MovementAction(-1, 0)


@pytest.fixture
def move_right() -> MovementAction:
    return MovementAction(1, 0)


@pytest.fixture
def player() -> Entity:
    return copy.deepcopy(entity_factories.player)


@pytest.fixture
def event_handler() -> EventHandler:
    return EventHandler()


@pytest.fixture
def game_map(player: Entity) -> GameMap:
    return generate_dungeon(30, 6, 10, 80, 45, 2, player)


@pytest.fixture
def engine(player: Entity, event_handler: EventHandler, game_map: GameMap) -> Engine:
    return Engine(event_handler, game_map, player)


class TestMovementAction:
    def test_perform(
        self,
        engine: Engine,
        player: Entity,
        move_up: MovementAction,
        move_down: MovementAction,
        move_left: MovementAction,
        move_right: MovementAction,
    ):
        init_x, init_y = player.x, player.y
        move_up.perform(engine, player)
        assert player.x == init_x
        assert player.y == init_y + 1
        move_down.perform(engine, player)
        assert player.x == init_x
        assert player.y == init_y
        move_left.perform(engine, player)
        assert player.x == init_x - 1
        assert player.y == init_y
        move_right.perform(engine, player)
        assert player.x == init_x
        assert player.y == init_y


class TestMeleeAction:
    def test_perform(
        self,
    ):
        pass
