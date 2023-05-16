from __future__ import annotations
from typing import TYPE_CHECKING

from lawrogue import color
from lawrogue.actions import Action, ItemAction
from lawrogue.components.base_component import BaseComponent
from lawrogue.exceptions import Impossible

if TYPE_CHECKING:
    from lawrogue.entity import Actor, Item


class Consumable(BaseComponent):
    parent: Item

    def get_action(self, consumer: Actor) -> Action | None:
        """
        Try to return the action for this item.
        """
        return ItemAction(consumer, self.parent)

    def activate(self, action: ItemAction) -> None:
        """
        Invoke this item's ability.

        `action` is the context for this activation
        """
        raise NotImplementedError()


class HealingConsumable(Consumable):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def activate(self, action: ItemAction) -> None:
        consumer = action.entity
        amount_recovered = consumer.fighter.heal(self.amount)

        if amount_recovered > 0:
            self.engine.message_log.add_message(
                f"You consume the {self.parent.name}, and recover {amount_recovered} HP!",
                color.health_recovered,
            )
        else:
            raise Impossible(f"Your health is already full.")
