from ex0 import Card
from ex2 import Combatable
from .Rankable import Rankable
from typing import Union


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        id: str,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        shield: int,
        rank: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        self.id = id
        self.looses = 0
        self.wins = 0
        self.damage = damage
        self.health = health
        self.shield = shield
        self.rank = rank

    def play(self, game_state: dict) -> dict:
        try:
            res: dict[str, int | str] = {}
            if game_state["mana"] < 2:
                raise Exception("Not enough mana")
            res["card_played"] = self.name
            res["mana_used"] = 2
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

    def calculate_rating(self) -> int:
        try:
            if self.wins == 0:
                return self.rank - self.looses * 10
            return self.rank + (int(self.wins / self.looses) * 10)
        except ZeroDivisionError:
            return self.rank + self.wins * 10
        except Exception as err:
            print(err)
            return self.rank

    def get_tournament_stats(self) -> dict:
        return {
            "Interfaces": "[Card, Combatable, Rankable]",
            "Rating": self.calculate_rating(),
            "Record": f"{self.wins}-{self.looses}",
        }

    def update_wins(self, wins: int) -> None:
        self.wins = wins

    def update_losses(self, losses: int) -> None:
        self.looses = losses

    def get_rank_info(self) -> dict:
        return {
            "wins": self.wins,
            "looses": self.looses,
            "rank": self.rank,
        }
