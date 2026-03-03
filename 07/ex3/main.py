from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggresiveStrategy import AgressiveStrategy


def main() -> None:
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    engine = GameEngine()
    engine.configure_engine(FantasyCardFactory(), AgressiveStrategy())
    print(f"Factory: {engine.factory.__class__.__name__}")
    print(f"Strategy: {engine.strategy.__class__.__name__}")
    print(f"Available types: {engine.factory.get_supported_types()}")
    print("\nSimulating aggressive turn...")
    actions = engine.simulate_turn()
    print("\nTurn execution:")
    print(f"Strategy: {engine.strategy.get_strategy_name()}")
    print(f"Actions: {actions}")
    print("\nGame Report:")
    print(f"{engine.get_engine_status()}")
    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
