from Card import Card
from typing import Dict, Union


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        try:
            res: dict[str, Union[int, str]] = {}
            if game_state["mana"] < 5:
                raise Exception("Not enough mana")
            res["card_played"] = self.name
            res["mana_used"] = 5
            res["effect"] = "Creature summoned to battlefield"
            return res
        except Exception as err:
            print(err)
            return {}

    def attack_target(self, target: str) -> dict:
        res: Dict[str, Union[int, str, bool]] = {}
        res["attacker"] = self.name
        res["target"] = target
        res["damage_dealt"] = self.attack
        res["combat_resolved"] = True
        return res
