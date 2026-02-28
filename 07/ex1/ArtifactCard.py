from ex0.Card import Card
from typing import Union


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        try:
            res: dict[str, Union[int, str]] = {}
            if game_state["mana"] < 2:
                raise Exception("Not enough mana")
            res["card_played"] = self.name
            res["mana_used"] = 2
            res["effect"] = self.effect
            return res
        except Exception as err:
            print(err)
            return {}

    def activate_ability(self) -> dict:
        pass
