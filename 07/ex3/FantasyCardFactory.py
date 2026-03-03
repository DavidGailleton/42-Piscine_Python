from .CardFactory import CardFactory
from random import choice
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard
from copy import deepcopy

creature_cards = [
    CreatureCard("Fire Dragon", 20, "Rare", 7, 20),
    CreatureCard("Goblin Warrior", 12, "Common", 4, 10),
]

spell_cards = [
    SpellCard("Fire Ball", 5, "Rare", "Decrase health by 1 for 3 round", 5),
    SpellCard("Ice Spike", 3, "Common", "Reduce damage by 2 for 1 round", 3),
    SpellCard(
        "Lightning bolt", 10, "Legendary", "Card can't play for 3 round", 10
    ),
]

artifact_cards = [
    ArtifactCard(
        "Mana Ring", 2, "Common", 3, "Increase mana by 1 for each round"
    ),
    ArtifactCard(
        "Witch Staff", 6, "Legendary", 5, "Decrease 5 mana of a card"
    ),
]


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        card = deepcopy(choice(creature_cards))
        if isinstance(name_or_power, str):
            card.name = name_or_power
        elif isinstance(name_or_power, int):
            card.attack = name_or_power
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        card = deepcopy(choice(spell_cards))
        if isinstance(name_or_power, str):
            card.name = name_or_power
        elif isinstance(name_or_power, int):
            card.mana = name_or_power
        return card

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        card = deepcopy(choice(artifact_cards))
        if isinstance(name_or_power, str):
            card.name = name_or_power
        elif isinstance(name_or_power, int):
            card.durability = name_or_power
        return card

    def create_themed_deck(self, size: int) -> dict:
        deck: dict[str, list[Card]] = {}
        for _ in range(size):
            card = choice(
                [
                    self.create_creature(),
                    self.create_artifact(),
                    self.create_spell(),
                ]
            )
            if card.name in deck:
                deck[card.name] += [card]
            else:
                deck[card.name] = [card]
        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": [card.name for card in creature_cards],
            "spells": [card.name for card in spell_cards],
            "artifacts": [card.name for card in artifact_cards],
        }
