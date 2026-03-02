from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: str) -> dict: ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict: ...

    @abstractmethod
    def get_combate_stats(self) -> dict: ...
