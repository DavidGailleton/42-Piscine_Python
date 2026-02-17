from abc import ABC, abstractmethod
from typing import Union


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        res = dict(self.__dict__)
        return res

    def is_playable(self, available_mana: int) -> bool:
        if available_mana > 5:
            return True
        return False
