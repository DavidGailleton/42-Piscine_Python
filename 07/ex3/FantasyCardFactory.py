from .CardFactory import CardFactory
from random import choice
from ex0 import Card, CreatureCard
from ex1 import SpellCard, ArtifactCard

creature_cards = [
    CreatureCard("Fire Dragon", 20, "Rare", 7, 20),
    CreatureCard("Goblin Warrior", 12, "Common", 4, 10),
]

spell_cards = [
    SpellCard("Fire Ball", 5, "Rare", "Decrase health by 1 for 3 round"),
    SpellCard("Ice Spike", 3, "Common", "Reduce damage by 2 for 1 round"),
    SpellCard(
        "Lightning bolt", 10, "Legendary", "Card can't play for 3 round"
    ),
]

artifact_cards = [
    ArtifactCard(
        "Mana Ring", 2, "Common", 3, "Increase mana by 1 for each round"
    ),
    ArtifactCard("Witch Staff", 6, "Legendary", 5, ""),
]


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        card = choice(creature_cards)
        if isinstance(name_or_power, str):
            card.name = name_or_power
        elif isinstance(name_or_power, int):
            card.attack = name_or_power
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return super().create_spell(name_or_power)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return super().create_artifact(name_or_power)

    def create_themed_deck(self, size: int) -> dict:
        return super().create_themed_deck(size)

    def get_supported_types(self) -> dict:
        return super().get_supported_types()
