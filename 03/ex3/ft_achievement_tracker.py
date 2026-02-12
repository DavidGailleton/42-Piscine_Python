def tracker_system(players: dict[str, list[str]]) -> None:
    print("=== Achievement Tracker System ===\n")
    try:
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
    except Exception as err:
        print(err)
    try:
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
        a_vs_b_common = set((players["alice"])) & set((players["bob"]))
        print(f"Alice vs Bob common: {a_vs_b_common}")
        alice_unique = set((players["alice"])) - set((players["bob"]))
        print(f"Alice unique: {alice_unique}")
        bob_unique = set((players["bob"])) - set((players["alice"]))
        print(f"Bob unique: {bob_unique}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    data = {
        "alice": [
            "first_blood",
            "pixel_perfect",
            "speed_runner",
            "first_blood",
            "first_blood",
            "boss_hunter",
        ],
        "bob": [
            "level_master",
            "boss_hunter",
            "treasure_seeker",
            "level_master",
            "level_master",
        ],
        "charlie": [
            "treasure_seeker",
            "boss_hunter",
            "combo_king",
            "first_blood",
            "boss_hunter",
            "first_blood",
            "boss_hunter",
            "first_blood",
        ],
        "diana": [
            "first_blood",
            "combo_king",
            "level_master",
            "treasure_seeker",
            "speed_runner",
            "combo_king",
            "combo_king",
            "level_master",
        ],
        "eve": [
            "level_master",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
        ],
        "frank": [
            "explorer",
            "boss_hunter",
            "first_blood",
            "explorer",
            "first_blood",
            "boss_hunter",
        ],
    }
    tracker_system(data)
