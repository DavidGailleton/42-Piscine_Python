from typing import Callable, Any
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def print_time(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}")
        start = time.time()
        res = func(args, kwargs)
        print(f"Spell completed int {time.time() - start} seconds")
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
    def validate_mage_name(name: str) -> bool: ...

    def cast_spell(self, spell_name: str, power: int) -> str: ...
