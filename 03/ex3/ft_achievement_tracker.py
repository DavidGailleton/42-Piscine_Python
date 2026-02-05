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
    common_achievements: set[str] = unique_achievements.intersection(players)
    print(f"\nCommon to all players: {common_achievements}")
    rare_achievements: set[str] = set(())
    for player in players:
        temp = set((players[player]))
        for other in players:
            if other != player:
                temp = temp - set((players[other]))
        rare_achievements = rare_achievements & temp
    print(f"Rare achievements (1 player): {rare_achievements}\n")


if __name__ == "__main__":
    players = {
            "Alice": ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
            "Bob": ['first_kill', 'level_10', 'boss_slayer', 'collector'],
            "Charlie": ['level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist']
    }
#    players = {'alice': ['first_blood', 'pixel_p:unique_achievementserfect', 'speed_runner', 'first_blood', 'first_blood'], 'bob': ['level_master', 'boss_hunter', 'treasure_seeker', 'level_master', 'level_master'], 'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king', 'first_blood', 'boss_hunter', 'first_blood', 'boss_hunter', 'first_blood'], 'diana': ['first_blood', 'combo_king', 'level_master', 'treasure_seeker', 'speed_runner', 'combo_king', 'combo_king', 'level_master'], 'eve': ['level_master', 'treasure_seeker', 'first_blood', 'treasure_seeker', 'first_blood', 'treasure_seeker'], 'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer', 'first_blood', 'boss_hunter']}
    tracker_system(players)
