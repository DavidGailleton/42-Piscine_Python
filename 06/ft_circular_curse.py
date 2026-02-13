def ingredients_validation() -> None:
    import alchemy.grimoire

    print(
        f'validate_ingredients("fire air"): {validate_ingredients("fire air")}'
    )


def main() -> None:
    ingredients_validation()


if __name__ == "__main__":
    main()
