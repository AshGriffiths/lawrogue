#!/usr/bin/env python
import copy
import traceback

import tcod

from lawrogue import color, entity_factories
from lawrogue.engine import Engine
from lawrogue.input_handlers import EventHandler
from lawrogue.procgen import generate_dungeon


def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    max_items_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
        engine=engine,
    )

    engine.update_fov()

    engine.message_log.add_message(
        "Hello and welcome, adventurer, to LAW rogue!", color.welcome_text
    )

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="LAW Rogue",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:
                traceback.print_exc()
                engine.message_log.add_message(traceback.format_exc, color.error)


if __name__ == "__main__":
    main()
