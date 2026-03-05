from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    platform = TournamentPlatform()
    print(
        platform.register_card(
            TournamentCard(
                "dragon_001", "Fire Dragon", 20, "Rare", 15, 25, 5, 1200
            )
        )
    )
    print(
        platform.register_card(
            TournamentCard(
                "wizard_001", "Ice Wizard", 15, "common", 10, 30, 4, 1150
            )
        )
    )
    print("Creating tournament match...")
    match_res = platform.create_match("dragon_001", "wizard_001")
    print(f"Math result: {match_res}\n")
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i in range(len(leaderboard)):
        print(f"{i + 1}. {leaderboard[i].name} - Rating:\
 {leaderboard[i].calculate_rating()}\
 ({leaderboard[i].get_tournament_stats()['Record']})")
    print("\nPlatform Report:")
    print(platform.generate_tournament_report())
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
