def ingredients_validation() -> None:
    from alchemy.grimoire.validator import validate_ingredients

    print(
        f'validate_ingredients("fire air"): {validate_ingredients("fire air")}'
    )
    print(
        f'validate_ingredients("dragon scale"): {validate_ingredients("dragon scale")}'
    )


def spell_recording_test() -> None:
    from alchemy.grimoire.spellbook import record_spell

    print(
        f'record_spell("Fireball", "fire air"): {record_spell("Fireball", "fire air")}'
    )
    print(
        f'record_spell("Dark Magic", "shadow"): {record_spell("Dark Magic", "shadow")}'
    )


def late_import_test() -> None:
    from alchemy.grimoire.spellbook import record_spell

    print(
        f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}'
    )


def main() -> None:
    print("=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    ingredients_validation()
    print("\nTesting spell recording with validation:")
    spell_recording_test()
    print("\nTesting late import technique:")
    late_import_test()
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
