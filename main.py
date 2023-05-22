#!/usr/bin/env python
import traceback

import tcod

from lawrogue import color
from lawrogue.exceptions import QuitWithoutSaving
from lawrogue.input_handlers import BaseEventHandler, EventHandler, MainGameEventHandler
from lawrogue.setup_game import MainMenu


def save_game(handler: BaseEventHandler, filename: str) -> None:
    """
    If the current event handler has an active Engine then save it.
    """
    if isinstance(handler, EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main():
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: BaseEventHandler = MainMenu()

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="LAW Rogue",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)
                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:
                    traceback.print_exc()
                    if isinstance(handler, EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc, color.error
                        )
        except QuitWithoutSaving:
            raise
        except SystemExit:
            save_game(handler, "savegame.sav")
            raise
        except BaseException:
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
