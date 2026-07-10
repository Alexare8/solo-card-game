from random import shuffle as randomShuffle

from card import Card, Suit

standardCardList = []
suits = [Suit.SPADES, Suit.DIAMONDS, Suit.CLUBS, Suit.HEARTS]
for suit in suits:
    for rank in range(1, 14):
        standardCardList.append((rank, suit))
standardCardList = standardCardList[:26] + standardCardList[38:25:-1] + standardCardList[51:38:-1]


class Deck:
    def __init__(self, cardList: list[tuple[int, Suit]] = standardCardList) -> None:
        self.cards = []
        for card in cardList:
            self.cards.append(Card(card[0], card[1]))

    def __str__(self) -> str:
        cardStrings = [str(card) for card in self.cards]
        return ", ".join(cardStrings)

    def __len__(self) -> int:
        return len(self.cards)

    def peekTop(self) -> Card:
        return self.cards[0]

    def draw(self) -> Card:
        return self.cards.pop(0)

    def shuffle(self) -> None:
        randomShuffle(self.cards)
