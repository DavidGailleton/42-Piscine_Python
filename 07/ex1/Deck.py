from ex0.Card import Card


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
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        pass
