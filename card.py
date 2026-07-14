class Card:
    def __init__(self, rank: int, printRank: str, suit: int, suitIcon: str) -> None:
        self.rank = rank
        self.printRank = printRank
        self.suit = suit
        self.suitIcon = suitIcon

    def __str__(self) -> str:
        return f"{self.printRank}{self.suitIcon}"

    def greaterThan(self, otherCard: Card) -> bool:
        if self.rank > otherCard.rank:
            return True
        if self.rank < otherCard.rank:
            return False
        if self.suit > otherCard.suit:
            return True
        return False

    def lessThan(self, otherCard: Card) -> bool:
        if self.rank < otherCard.rank:
            return True
        if self.rank > otherCard.rank:
            return False
        if self.suit < otherCard.suit:
            return True
        return False
