from random import shuffle as randomShuffle

from card import Card


class Deck:
    def __init__(self, ranks: list[tuple], suits: list[tuple]) -> None:
        self.cards = []
        self.populate(ranks, suits)

    def __str__(self) -> str:
        cardStrings = [str(card) for card in self.cards]
        return ", ".join(cardStrings)

    def __len__(self) -> int:
        return len(self.cards)

    def peekTop(self) -> Card:
        return self.cards[0]

    def draw(self) -> Card:
        return self.cards.pop(0)

    def populate(self, ranks, suits) -> None:
        for rank, printRank in ranks:
            for suit, icon in suits:
                self.cards.append(Card(rank, printRank, suit, icon))

    def shuffle(self) -> None:
        randomShuffle(self.cards)
