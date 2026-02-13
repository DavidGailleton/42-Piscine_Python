def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_res = validate_ingredients(ingredients)
    if validation_res == f"{ingredients} - VALID":
        return f"Spell recorded: {spell_name} ({validation_res})"
    else:
        return f"Spell rejected: {spell_name} ({validation_res})"
