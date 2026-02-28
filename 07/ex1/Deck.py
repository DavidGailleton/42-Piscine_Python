from ex0 import Card, CreatureCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards += [card]

    def remove_card(self, card_name: Card) -> None:
        for n in range(len(self.cards)):
            if self.cards[n].name == card_name:
                self.cards.pop(n)
                return
        print("{card_name} not found")

    def shuffle(self) -> None:
        from random import shuffle

        shuffle(self.cards)

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        from . import ArtifactCard, SpellCard

        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0.0
        for card in self.cards:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            elif isinstance(card, SpellCard):
                spells += 1
            total_cost += card.cost
        return {
            "total_card": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": total_cost / len(self.cards),
        }
