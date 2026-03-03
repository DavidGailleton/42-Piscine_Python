from .GameStrategy import GameStrategy
from operator import attrgetter


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return {
            "cards_played": [card.name for card in hand],
            "mana_used": 5,
            "targets_attacked": battlefield,
            "damage_dealt": 8,
        }

    def get_strategy_name(self) -> str:
        return "Aggressive"

    def prioritize_targets(self, available_targets: list) -> list:
        try:
            return sorted(available_targets, key=attrgetter("health"))
        except Exception as err:
            print(err)
            return available_targets
