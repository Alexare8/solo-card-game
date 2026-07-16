class Card:
    def __init__(self, rank: int, print_rank: str, suit: int, suit_icon: str) -> None:
        self.rank = rank
        self.print_rank = print_rank
        self.suit = suit
        self.suit_icon = suit_icon

    def __str__(self) -> str:
        return f"{self.print_rank}{self.suit_icon}"

    def greater_than(self, other_card: "Card") -> bool:
        if self.rank > other_card.rank:
            return True
        if self.rank < other_card.rank:
            return False
        if self.suit > other_card.suit:
            return True
        return False

    def less_than(self, other_card: "Card") -> bool:
        if self.rank < other_card.rank:
            return True
        if self.rank > other_card.rank:
            return False
        if self.suit < other_card.suit:
            return True
        return False
