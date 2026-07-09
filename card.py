from enum import Enum
from random import choice, randint


class Suit(Enum):
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    HEARTS = 4


class Card:
    def __init__(self, rank: int, suit: Suit) -> None:
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.printRankLetter()}{self.printSuitIcon()}"

    def printRankLetter(self) -> str:
        match self.rank:
            case 1:
                return "A"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case _:
                return str(self.rank)

    def printSuitIcon(self) -> str:
        match self.suit:
            case Suit.SPADES:
                return "♠"
            case Suit.DIAMONDS:
                return "♦"
            case Suit.CLUBS:
                return "♣"
            case Suit.HEARTS:
                return "♥"


def randomCard() -> Card:
    rank = randint(1, 13)
    suit = choice([Suit.SPADES, Suit.DIAMONDS, Suit.CLUBS, Suit.HEARTS])
    return Card(rank, suit)


def main():
    output = ""
    for _ in range(5):
        output += f" {randomCard()}"

    print(output)
