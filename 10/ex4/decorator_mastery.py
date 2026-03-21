from typing import Callable, Any
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def print_time(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}")
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Spell completed int {(time.time() - start):.3f} seconds")
        return res

    return print_time


def power_validator(min_power: int) -> Callable:
    def check_power(power: int, func: Callable) -> str | Any:
        try:
            if power < min_power:
                return "Insufficient power for this spell"
            return func()
        except Exception:
            return "invalid input"

    return check_power


def retry_spell(max_attempts: int) -> Callable:
    def try_spell(func: Callable) -> str | Any:
        for i in range(max_attempts):
            try:
                return func()
            except Exception:
                print(f"Spell failed, retrying... ({i + 1}/{max_attempts})")
                continue
        return f"Spell casting failed after {max_attempts} attempts"

    return try_spell


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(x.isalpha() or x.isspace() for x in name)

    def cast_spell(self, spell_name: str, power: int) -> str:
        def cast() -> str:
            return f"Successfully cast {spell_name} with {power} power"

        validator = power_validator(10)
        return validator(power, cast)


def main() -> None:
    def fireball() -> str:
        return "Fireball cast!"

    def make_exception() -> None:
        raise Exception

    print("===spell_timer===\n")
    timer = spell_timer(fireball)
    print(f"Result: {timer()}")

    print("\n===power_validator===\n")
    validator = power_validator(10)
    print(f"Valid: {validator(15, fireball)}")
    print(f"Invalid: {validator(5, fireball)}")

    print("\n===retry_spell===\n")
    retry = retry_spell(3)
    print(f"Valid: {retry(fireball)}")
    print(f"Invalid: {retry(make_exception)}")

    print("\n======MageGuild======\n")
    print("\n===validate_mage_name===\n")
    print(f"Less than 3 chars: {MageGuild.validate_mage_name('op')}")
    print(f"Special char: {MageGuild.validate_mage_name('ope!')}")
    print(
        "valid: "
        f"{MageGuild.validate_mage_name('Bonjour a tous c est vendredi')}"
    )

    print("\n===cast_spell===\n")
    guild = MageGuild()
    print(f"Valid: {guild.cast_spell('Lightning', 15)}")
    print(f"Invalid: {guild.cast_spell('Lightning', 5)}")


if __name__ == "__main__":
    main()
