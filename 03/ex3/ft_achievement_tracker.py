class Player:
    __name: str
    __achievements: set[str]

    def __init__(self, name:str, achievements: set[str]) -> None:
        self.__name = name
        self.__achievements = achievements

    def get_name(self) -> str:
        return self.__name

    def get_achievements(self) -> set[str]:
        return self.__achievements


if __name__ == "__main__":
    players = [
        Player("Alice", set(('first_kill', 'level_10', 'treasure_hunter', 'speed_demon'))),
        Player("Bob",set(('first_kill', 'level_10', 'boss_slayer', 'collector'))),
        Player("Charlie", set(('level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist')))
    ]
    print("=== Achievement Tracker System ===\n")
    for n in players:
        print(f"Player {n.get_name()} achievements: {n.get_achievements()}")
    print("\n=== Achievement Analytics ===")
    unique_achievements = players[0].get_achievements() | players[1].get_achievements() | players[2].get_achievements()
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    common_achievements = players[0].get_achievements() & players[1].get_achievements() & players[2].get_achievements()
    print(f"\nCommon to all players: {common_achievements}")
    p0_achievements = players[0].get_achievements() - players[1].get_achievements() - players[2].get_achievements()
    p1_achievements = players[0].get_achievements() - players[1].get_achievements() - players[2].get_achievements()
    p2_achievements = players[0].get_achievements() - players[1].get_achievements() - players[2].get_achievements()
    print(f"Rare achievements (1 player): {rare_achievements}")

