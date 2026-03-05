from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []
        self.math_played = 0

    def register_card(self, card: TournamentCard) -> str:
        try:
            stats = card.get_tournament_stats()
            res = f"{card.name} (ID: {card.id}):\n\
- Interfaces: {stats['Interfaces']}\n\
- Rating: {stats['Rating']}\n\
- Record: {stats['Record']}\n"
            self.cards += [card]
            return res
        except Exception:
            print("Invalid card")
            return "error"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        from random import shuffle

        try:
            cards = [
                card
                for card in self.cards
                if card.id == card1_id or card.id == card2_id
            ]
            if len(cards) != 2:
                raise Exception(
                    "At least once of cards id provide isn't in platform"
                )
            shuffle(cards)
            winner = cards.pop()
            loser = cards.pop()
            winner.update_wins(winner.wins + 1)
            loser.update_losses(loser.looses + 1)
            self.math_played += 1
            return {
                "winner": winner.id,
                "loser": loser.id,
                "winner_rating": winner.calculate_rating(),
                "loser_rating": loser.calculate_rating(),
            }
        except Exception as err:
            print(err)
            return {}

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards, key=lambda x: x.calculate_rating(), reverse=True
        )

    def generate_tournament_report(self) -> dict:
        return {
            "total_cards": len(self.cards),
            "mathes_played": self.math_played,
            "avg_rating": int(
                sum([card.calculate_rating() for card in self.cards])
                / len(self.cards)
            ),
            "platform_status": "active",
        }
