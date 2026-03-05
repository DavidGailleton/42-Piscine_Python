def main() -> None:
    from .Deck import Deck
    from .SpellCard import SpellCard
    from .ArtifactCard import ArtifactCard
    from ex0 import CreatureCard

    print("=== DataDeck Deck Builder ===\n")
    deck = Deck()
    print("Building deck with different card types...")
    deck.add_card(
        SpellCard("Lightning Bolt", 5, "Common", "Deal 3 dammage to target", 5)
    )
    deck.add_card(
        ArtifactCard(
            "Mana Crystal", 7, "Medium", 1, "Permanent: +1 mana per turn"
        )
    )
    deck.add_card(CreatureCard("Fire dragon", 10, "Rare", 15, 20))
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("\nDrawing and playing cards:\n")
    for _ in range(deck.get_deck_stats()["total_card"]):
        try:
            card = deck.draw_card()
            print(f"Drew: {card.name} ({card.__class__.__name__})")
            print(f"{card.play({'mana': 5})}\n")
        except Exception as err:
            print(err)
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
