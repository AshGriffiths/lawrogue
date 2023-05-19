from __future__ import annotations
from typing import TYPE_CHECKING

from lawrogue import color
from lawrogue.actions import Action, ItemAction
from lawrogue.components.base_component import BaseComponent
from lawrogue.components.inventory import Inventory
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

    def consume(self) -> None:
        """
        Remove the consumed item from its containing inventory.
        """
        entity = self.parent
        inv = entity.parent
        if isinstance(inv, Inventory):
            inv.items.remove(entity)


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
            self.consume()
        else:
            raise Impossible(f"Your health is already full.")


class LightningDamageConsumable(Consumable):
    def __init__(self, damage: int, maximum_range: int) -> None:
        self.damage = damage
        self.maximum_range = maximum_range

    def activate(self, action: ItemAction) -> None:
        consumer = action.entity
        target = None
        closest_distance = self.maximum_range + 1.0

        for actor in self.engine.game_map.actors:
            if actor is not consumer and self.parent.game_map.visible[actor.x, actor.y]:
                distance = consumer.distance(actor.x, actor.y)

                if distance < closest_distance:
                    target = actor
                    closest_distance = distance

        if target:
            self.engine.message_log.add_message(
                f"A lightning bolt strikes the {target.name} with a loud thunder for {self.damage} damage!"
            )
            target.fighter.take_damage(self.damage)
            self.consume()
        else:
            raise Impossible("No enemy is close enough to strike.")
