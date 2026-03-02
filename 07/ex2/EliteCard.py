from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical
from typing import Union


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        shield: int,
        initial_mana: int,
        spell_cost: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.shield = shield
        self.mana = initial_mana
        self.spell_cost = spell_cost

    def play(self, game_state: dict) -> dict:
        try:
            res: dict[str, int | str] = {}
            if game_state["mana"] < 5:
                raise Exception("Not enough mana")
            res["card_played"] = self.name
            res["mana_used"] = 5
            res["effect"] = "Creature summoned to battlefield"
            return res
        except Exception as err:
            print(err)
            return {}

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.damage,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        res: dict[str, Union[str, int, bool]] = {}
        res["defender"] = self.name
        if incoming_damage <= self.shield:
            res["damage_blocked"] = incoming_damage
            res["damage_taken"] = 0
        else:
            res["damage_taken"] = incoming_damage - self.shield
            res["damage_blocked"] = self.shield
            self.health -= incoming_damage - self.shield
        res["still_alive"] = self.health > 0
        return res

    def get_combate_stats(self) -> dict:
        return {
            "damage": self.damage,
            "health": self.health,
            "shield": self.shield,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        try:
            if self.mana < self.spell_cost:
                raise Exception("Not enough mana")
            self.mana -= self.spell_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": self.spell_cost,
            }
        except Exception as err:
            print(err)
            return {}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana, "spell cost": self.spell_cost}
