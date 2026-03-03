from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.turns_simulated = 0
        self.total_damage = 0
        self.created_cards = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        try:
            cards = []
            deck = self.factory.create_themed_deck(3).values()
            for card_list in deck:
                for card in card_list:
                    cards += [card]
            hand = [f"{card.name} ({card.cost})" for card in cards]
            print(f"Hand: {hand}")
            turn = self.strategy.execute_turn(cards, ["Enemy player"])
            self.total_damage += turn["damage_dealt"]
            self.created_cards += 3
            self.turns_simulated += 1
            return turn
        except Exception as err:
            print(err)
            return {}

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.created_cards,
        }
