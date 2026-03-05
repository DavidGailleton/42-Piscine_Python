def main() -> None:
    from .EliteCard import EliteCard

    print("=== DataDeck Ability System ===\n")
    card = EliteCard("Arcane Warrior", 25, "Legendary", 5, 20, 3, 4, 4)
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {card.attack('Enemy')}")
    print(f"Defense result: {card.defend(5)}")
    print("\nMagic phase:")
    print(f"Spell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {card.channel_mana(3)}")
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
