from ex0.Card import Card
from typing import Union


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
         try:
            res: dict[str, Union[int, str]] = {}
            if game_state["mana"] < 3:
                raise Exception("Not enough mana")
            res["card_played"] = self.name
            res["mana_used"] = 3
            res["effect"] = self.effect_type
            return res
        except Exception as err:
            print(err)
            return {}

   def resolve_effect(self, targets: list) -> dict:
        pass
