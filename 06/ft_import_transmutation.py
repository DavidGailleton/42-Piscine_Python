def full_module_import() -> None:
    import alchemy.elements

    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def specific_function_import() -> None:
    from alchemy.elements import create_water

    print(f"create_water(): {create_water()}")


def aliased_import() -> None:
    from alchemy.potions import healing_potion as heal

    print(f"heal(): {heal()}")


def multiple_import() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion

    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def main() -> None:
    print("=== Import Transmutation Mastery ===\n")
    print("Method 1 - Full module import:")
    try:
        full_module_import()
    except Exception as err:
        print(err)
    print("\nMethod 2 - Specific function import:")
    try:
        specific_function_import()
    except Exception as err:
        print(err)
    print("\nMethod 3 - Aliased import:")
    try:
        aliased_import()
    except Exception as err:
        print(err)
    print("\nMethod 4 - Multiple imports:")
    try:
        multiple_import()
    except Exception as err:
        print(err)
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    main()
