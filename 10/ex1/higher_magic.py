from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(*args):
        return (spell1(*args), spell2(*args))

    return combiner


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplie(*args):
        return base_spell(*args) * multiplier

    return multiplie


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cond_res(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(args[0])
        else:
            return "Spell fizzled"

    return cond_res


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        return [res(*args, **kwargs) for res in spells]

    return sequence


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def pow_2(nb: int) -> int:
    return nb * nb


def main() -> None:
    try:
        print("=== spell_combiner ===")
        combiner = spell_combiner(fireball, heal)
        print(f"Combine fireball and heal: {combiner('dragon')}")

        print("\n=== power_amplifier ===")
        amplifier = power_amplifier(pow_2, 4)
        print(f"multiplie 5 pow_2 by 4: {amplifier(5)}")

        print("\n=== conditional_caster ===")
        caster = conditional_caster(isinstance, fireball)
        print(f"Valid: {caster('dragon', str)}")
        print(f"Invalid: {caster(2, str)}")

        print("\n=== spell_sequence ===")
        sequencer = spell_sequence([fireball, heal, isinstance])
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
