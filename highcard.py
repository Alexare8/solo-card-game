from deck import Deck
from card import Card


def display_hand(hand: list[Card]) -> str:
    cards = [str(card) for card in hand]
    return "Hand: " + ", ".join(cards)


def game() -> int:
    HAND_SIZE = 2
    if HAND_SIZE < 1:
        raise ValueError("Minimum HAND_SIZE is 1")

    RANKS = [(1,"A"), (2,"2"), (3,"3"), (4,"4"), (5,"5"), (6,"6"), (7,"7"),
                 (8,"8"), (9,"9"), (10,"10"), (11,"J"), (12,"Q"), (13,"K")]
    SUITS = [(4,"♠"), (3,"♦"), (2,"♣"), (1,"♥")]
    deck = Deck(RANKS, SUITS)
    deck.shuffle()
    hand = [deck.draw() for _ in range(HAND_SIZE)]

    print(f"You draw {HAND_SIZE} cards.")
    print(display_hand(hand))
    selection = ""
    while True:
        selection = input(f"Select a card (1-{len(hand)}): ")
        if selection.isnumeric():
            selection = int(selection)
            if selection in range(1, len(hand)+1):
                break
    played_card = hand[selection-1]
    print(f"Your card is {played_card}. Top card is {deck.peek_top()}.")
    if played_card.greater_than(deck.peek_top()):
        print("You win!")
        return 1
    print("You lose!")
    return 0

def play() -> None:
    print("Welocme to High Card!")
    print("Select the card you wish to play from your hand. If it's higher than the card on top of the deck, you win!")

    keep_playing = True
    score = 0
    while keep_playing:
        score += game()
        print(f"Score: {score}")
        while True:
            replay = input("Play again? Y/N: ")
            if replay.upper() == "Y" or replay == "":
                break
            elif replay.upper() == "N":
                keep_playing = False
                break

if __name__ == '__main__':
    play()
