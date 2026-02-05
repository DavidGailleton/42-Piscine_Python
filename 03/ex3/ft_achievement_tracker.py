def tracker_system(players: dict[str, list[str]]) -> None:
    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player} achievements: {set((players[player]))}")
    print("\n=== Achievement Analytics ===")
    unique_achievements: set[str] = set(())
    for player in players:
        unique_achievements = unique_achievements | set((players[player]))
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    common_achievements: set[str] = unique_achievements
    for player in players:
        common_achievements = common_achievements & set((players[player]))
    print(f"\nCommon to all players: {common_achievements}")
    player_rare: dict[str, set[str]] = {}
    for player in players:
        temp = set((players[player]))
        for other in players:
            if other != player:
                temp = temp - set((players[other]))
        player_rare[player] = temp
    rare_achievements: set[str] = set(())
    for n in player_rare:
        rare_achievements = rare_achievements | player_rare[n]
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    a_vs_b_common = set((players["Alice"])) & set((players["Bob"]))
    print(f"Alice vs Bob common: {a_vs_b_common}")
    alice_unique = set((players["Alice"])) - set((players["Bob"]))
    print(f"Alice unique: {alice_unique}")
    bob_unique = set((players["Bob"])) - set((players["Alice"]))
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    players = {
            "Alice": ['first_kill', 'level_10',
                      'treasure_hunter', 'speed_demon'],
            "Bob": ['first_kill', 'level_10', 'boss_slayer', 'collector'],
            "Charlie": ['level_10', 'treasure_hunter', 'boss_slayer',
                        'speed_demon', 'perfectionist']
    }
    tracker_system(players)
