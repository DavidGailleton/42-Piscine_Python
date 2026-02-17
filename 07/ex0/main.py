def main():
    from CreatureCard import CreatureCard

    game_state = {"player": "michel", "mana": 6}
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"CreatureCard info:\n{creature_card.get_card_info()}")
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {creature_card.is_playable(game_state['mana'])}")
    print(f"Play result: {creature_card.play(game_state)}")
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creature_card.attack_target('Goblin Warrior')}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {creature_card.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
