from functools import lru_cache, reduce, partial, singledispatch
import operator as op
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: op.add(x, y), spells)
    if operation == "multiply":
        return reduce(lambda x, y: op.mul(x, y), spells)
    if operation == "max":
        return reduce(lambda x, y: x if x > y else y, spells)
    if operation == "min":
        return reduce(lambda x, y: x if x < y else y, spells)

    return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="lightning"
        ),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def basic(arg: Any) -> Any:
        return arg

    @basic.register(int)
    def basic_int(arg: int) -> str:
        return f"{arg} damage take"

    @basic.register(str)
    def basic_str(arg: str) -> str:
        return f"apply {arg}"

    @basic.register(list)
    def basic_list(arg: list[Any]) -> str:
        res = ""
        for cast in arg:
            res += f"cast {cast}\n"
        return res

    return basic


def attack(target: str, power: int, element: str) -> str:
    return f"{target}: take {power} damage, {element} is applied"


@lru_cache(maxsize=128)
def main() -> None:
    print("===spell_reducer===\n")
    print(f"sum of [4, 5, 6]: {spell_reducer([4, 5, 6], 'add')}")
    print(f"multiply [4, 5, 6]: {spell_reducer([4, 5, 6], 'multiply')}")
    print(f"max of [4, 5, 6]: {spell_reducer([4, 5, 6], 'max')}")
    print(f"min of [4, 5, 6]: {spell_reducer([4, 5, 6], 'min')}")

    print("\n===partial_enchanter===\n")
    attacks = partial_enchanter(attack)
    for x in attacks:
        print(f"{x}: {attacks[x]('goblin')}")

    print("\n===memoized_fibonacci===\n")
    print(f"fib(0): {memoized_fibonacci(0)}")
    print(f"fib(1): {memoized_fibonacci(1)}")
    print(f"fib(5): {memoized_fibonacci(5)}")
    print(f"fib(30): {memoized_fibonacci(30)}")

    print("\n===spell_dispatcher===\n")
    dispatcher = spell_dispatcher()
    print(f"int: {dispatcher(3)}")
    print(f"str: {dispatcher('fire')}")
    print(f"list: {dispatcher(['test', 'hello', 'world', '!'])}")
    print(f"dict: {dispatcher({1: 3})}")


if __name__ == "__main__":
    main()
