from typing import Callable, Any
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def print_time(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}")
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Spell completed int {(time.time() - start):.3f} seconds")
        return res

    return print_time


def power_validator(min_power: int) -> Callable:
    def check_power(func: Callable) -> str | Any:
        @wraps(func)
        def fn(*args: Any) -> str | Any:
            try:
                if args[2] < min_power:
                    return "Insufficient power for this spell"
                return func(*args)
            except Exception as err:
                print(err)
                return "invalid input"

        return fn

    return check_power


def retry_spell(max_attempts: int) -> Callable:
    def try_spell(func: Callable) -> str | Any:
        @wraps(func)
        def fn(*args: Any) -> Any:
            for i in range(max_attempts):
                try:
                    return func(*args)
                except Exception:
                    print(
                        f"Spell failed, retrying... ({i + 1}/{max_attempts})"
                    )
                    continue
            return f"Spell casting failed after {max_attempts} attempts"

        return fn

    return try_spell


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(x.isalpha() or x.isspace() for x in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    import time

    @spell_timer
    def fireball() -> str:
        time.sleep(0.5)
        return "Fireball cast!"

    @retry_spell(3)
    def make_exception(exception: Exception) -> None:
        raise exception

    guild = MageGuild()

    print("===spell_timer===\n")
    print(f"Result: {fireball()}")

    print("\n===power_validator===\n")
    print(f"Valid: {guild.cast_spell('meteorite de caca', 15)}")
    print(f"INvalid: {guild.cast_spell('meteorite de caca', 5)}")

    print("\n===retry_spell===\n")
    print(f"Invalid: {make_exception(Exception())}")

    print("\n======MageGuild======\n")
    print("\n===validate_mage_name===\n")
    print(f"Less than 3 chars: {MageGuild.validate_mage_name('op')}")
    print(f"Special char: {MageGuild.validate_mage_name('ope!')}")
    print(
        "valid: "
        f"{MageGuild.validate_mage_name('Bonjour a tous c est vendredi')}"
    )

    print("\n===cast_spell===\n")
    print(f"Valid: {guild.cast_spell('Lightning', 15)}")
    print(f"Invalid: {guild.cast_spell('Lightning', 5)}")


if __name__ == "__main__":
    main()
