from typing import Callable


def mage_counter() -> Callable:
    i = 0

    def count_call() -> int:
        nonlocal i
        i += 1
        return i

    return count_call


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def add_power(power_to_add: int) -> int:
        nonlocal power
        power += power_to_add
        return power

    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"

    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(to_store: dict[str, str]) -> None:
        for data in to_store:
            storage[data] = to_store[data]

    def recall(key: str) -> str:
        try:
            return storage[key]
        except KeyError:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("===mage_counter===\n")
    count = mage_counter()
    print(f"1 : {count()}")
    print(f"2 : {count()}")
    print(f"3 : {count()}")
    print(f"4 : {count()}")

    print("\n===spell_accumulator===\n")
    accumulator = spell_accumulator(30)
    print(f"initial_power: {accumulator(0)}")
    print(f"add 10: {accumulator(10)}")
    print(f"add 15: {accumulator(15)}")
    print(f"add 5: {accumulator(5)}")

    print("\n===enchantment_factory===\n")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(f"Flaming factory: {flaming('Sword')}")
    print(f"Frozen factory: {frozen('Shield')}")

    print("\n===memory_vault===\n")
    vault = memory_vault()
    vault["store"]({"name": "Jean", "surname": "Dupont"})
    print(f"Access to name: {vault['recall']('name')}")
    print(f"Access to age: {vault['recall']('age')}")


if __name__ == "__main__":
    main()
