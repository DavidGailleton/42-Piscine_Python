def validate_ingredients(ingredients: str) -> str:
    try:
        for ingredient in ingredients.split(" "):
            if ingredient not in ["fire", "water", "earth", "air"]:
                raise ValueError
        return f"{ingredients} - VALID"
    except ValueError:
        return f"{ingredients} - INVALID"
