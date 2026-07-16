from random import shuffle as random_shuffle

from card import Card


class Deck:
    def __init__(self, ranks: list[tuple], suits: list[tuple]) -> None:
        self.cards = []
        self.populate(ranks, suits)

    def __str__(self) -> str:
        card_strings = [str(card) for card in self.cards]
        return ", ".join(card_strings)

    def __len__(self) -> int:
        return len(self.cards)

    def peek_top(self) -> Card:
        return self.cards[0]

    def draw(self) -> Card:
        return self.cards.pop(0)

    def populate(self, ranks, suits) -> None:
        for rank, print_rank in ranks:
            for suit, icon in suits:
                self.cards.append(Card(rank, print_rank, suit, icon))

    def shuffle(self) -> None:
        random_shuffle(self.cards)
