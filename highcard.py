from deck import Deck
from card import Card


def displayHand(hand: list[Card]) -> str:
    cards = [str(card) for card in hand]
    return "Hand: " + ", ".join(cards)


def compareCards(cardOne: Card, cardTwo: Card) -> bool:
    if cardOne == cardTwo:
        raise ValueError("Identical cards being compared.")
    if cardOne.rank > cardTwo.rank:
        return True
    if cardOne.rank < cardTwo.rank:
        return False
    if cardOne.suit > cardTwo.suit:
        return True
    return False


def game() -> int:
    HAND_SIZE = 1
    if HAND_SIZE < 1:
        raise ValueError("Minimum HAND_SIZE is 1")

    deck = Deck()
    deck.shuffle()
    hand = [deck.draw() for _ in range(HAND_SIZE)]

    print(f"You draw {HAND_SIZE} cards.")
    print(displayHand(hand))
    selection = ""
    while True:
        selection = input(f"Select a card (1-{len(hand)}): ")
        if selection.isnumeric():
            selection = int(selection)
            if selection in range(1, len(hand)+1):
                break
    playedCard = hand[selection-1]
    print(f"Your card is {playedCard}. Top card is {deck.peekTop()}.")
    if compareCards(playedCard, deck.peekTop()):
        print("You win!")
        return 1
    print("You lose!")
    return 0

def main() -> None:
    print("Welocme to High Card!")
    print("Select the card you wish to play from your hand. If it's higher than the card on top of the deck, you win!")

    keepPlaying = True
    score = 0
    while keepPlaying:
        score += game()
        print(f"Score: {score}")
        while True:
            replay = input("Play again? Y/N: ")
            if replay.upper() == "Y" or replay == "":
                break
            elif replay.upper() == "N":
                keepPlaying = False
                break

if __name__ == '__main__':
    main()
