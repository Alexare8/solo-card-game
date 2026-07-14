from deck import Deck
from card import Card
from loboRules import RULES
import sys


def parseInput(options: list[str], message: str = "") -> str:
    while True:
        rawInputString = input(message)
        inputString = rawInputString.lower()
        if inputString in ["exit", "quit", "q"]:
            sys.exit()
        elif inputString in options:
            return inputString


def selectCard(cardList: list[Card]) -> Card:
    selection = parseInput([str(card.rank) for card in cardList], "Enter a card rank: ")
    selection = int(selection)
    for card in cardList:
        if card.rank == selection:
            return card


def selectMultipleCards(sourceList: list[Card]) -> list[Card]:
    selection = []
    cardList = [card for card in sourceList]
    firstCard = selectCard(cardList)
    selection.append(firstCard)
    cardList.remove(firstCard)
    print(f"Selected Total: {sum([card.rank for card in selection])}. Cards: {", ".join([str(card) for card in cardList])}.")
    secondCard = selectCard(cardList)
    selection.append(secondCard)
    cardList.remove(secondCard)
    selectAgain = True
    while selectAgain:
        if len(cardList) == 0:
            break
        print(f"Selected Total: {sum([card.rank for card in selection])}. Cards: {", ".join([str(card) for card in cardList])}.")
        cardInput = parseInput([str(card.rank) for card in cardList] + [""], "Press Enter to stop or enter a card rank: ")
        anotherCard = None
        if cardInput == "":
            selectAgain = False
        else:
            for card in cardList:
                if card.rank == int(cardInput):
                    anotherCard = card
            selection.append(anotherCard)
            cardList.remove(anotherCard)
    return selection


def round() -> tuple[bool, int]:
    RANKS = [(num, str(num)) for num in range(1, 11)]
    SUITS = [(5, "★"), (4,"♠"), (3,"♦"), (2,"♣"), (1,"♥")]
    deck = Deck(RANKS, SUITS)
    deck.shuffle()
    playerHand = [deck.draw() for _ in range(4)]
    wolfHand = [deck.draw() for _ in range(4)]

    continueRound = True
    while continueRound:
        try:
            print(f"Wolf hand: {", ".join([str(card) for card in wolfHand])}")
            print(f"Your hand: {", ".join([str(card) for card in playerHand])}")
            print(f"Top card: {deck.peekTop()}")
            match parseInput(["perfect", "sum", "split", "over", "fold"], "PERFECT, SUM, SPLIT, OVER, or FOLD? "):

                case "perfect":
                    print("Select a card from your hand: ")
                    playedCard = selectCard(playerHand)
                    targetedCard = None
                    cardMatch = False
                    for wolfCard in wolfHand:
                        if playedCard.rank == wolfCard.rank:
                            cardMatch = True
                            targetedCard = wolfCard
                            wolfHand.remove(wolfCard)
                    if cardMatch:
                        playerHand.remove(playedCard)
                    else:
                        raise ValueError("No PERFECT matching card in Wolf's hand.")

                    print(f"{playedCard} removes {targetedCard}.")
                    newCard = deck.draw()
                    playerHand.append(newCard)
                    print(f"You get {newCard}.")

                case "sum":
                    print("Select cards from your hand: ")
                    playedCards = selectMultipleCards(playerHand)
                    targetedCard = None
                    total = sum([card.rank for card in playedCards])
                    cardMatch = False
                    for wolfCard in wolfHand:
                        if total == wolfCard.rank:
                            cardMatch = True
                            targetedCard = wolfCard
                            wolfHand.remove(wolfCard)
                            break
                    if cardMatch:
                        for card in playedCards:
                            playerHand.remove(card)
                    else:
                        raise ValueError(f"No card in Wolf's hand matching SUM {total}.")

                    print(f"{", ".join([str(card) for card in playedCards])} removes {targetedCard}.")
                    newCard = deck.draw()
                    playerHand.append(newCard)
                    print(f"You get {newCard}.")

                case "split":
                    print("Select cards from the Wolf's hand: ")
                    playedCard = None
                    targetedCards = selectMultipleCards(wolfHand)
                    total = sum([card.rank for card in targetedCards])
                    cardMatch = False
                    for playerCard in playerHand:
                        if total == playerCard.rank:
                            cardMatch = True
                            playedCard = playerCard
                            playerHand.remove(playerCard)
                            break
                    if cardMatch:
                        for card in targetedCards:
                            wolfHand.remove(card)
                    else:
                        raise ValueError(f"No card in your hand matching SPLIT {total}.")

                    print(f"{playedCard} removes {", ".join([str(card) for card in targetedCards])}.")
                    newCard = deck.draw()
                    wolfHand.append(newCard)
                    print(f"The Wolf gets {newCard}.")

                case "over":
                    print("Select a card from your hand: ")
                    playedCard = selectCard(playerHand)
                    print("Select a card from the Wolf's hand: ")
                    targetedCard = selectCard(wolfHand)
                    if not playedCard.greaterThan(targetedCard):
                        raise ValueError(f"{playedCard} is not greater than {targetedCard}.")
                    difference = playedCard.rank - targetedCard.rank
                    playerHand.remove(playedCard)
                    wolfHand.remove(targetedCard)

                    print(f"{playedCard} removes {targetedCard}.")
                    for _ in range(difference):
                        newCard = deck.draw()
                        print(f"The Wolf gets {newCard}.")
                        wolfHand.append(newCard)

                case "fold":
                    continueRound = False

            print("")
            if len(playerHand) == 0 or len(wolfHand) == 0:
                continueRound = False

        except Exception as e:
            print(f"Error: {e}")


    if len(wolfHand) == 0:
        score = sum([card.rank for card in playerHand])
        print(f"You win the round! You score {score} points.")
        return (True, score)
    else:
        score = sum([card.rank for card in wolfHand])
        print(f"You lose the round. The Wolf scores {score} points.")
        return (False, score)


def game() -> None:
    playerScore = 0
    wolfScore = 0
    while (playerScore < 100 and wolfScore < 100):
        result = round()
        if result[0]:
            playerScore += result[1]
        else:
            wolfScore += result[1]
        print(f"You: {playerScore} Wolf: {wolfScore}\n")
    if wolfScore > 100:
        print("You lose.")
    else:
        print("You win!")


def play() -> None:
    print("Welocme to Lobo!")
    startInput = parseInput(["rules", ""], "Press Enter to begin a game. Type Rules for an explanation. Type Quit to quit.\n")
    if startInput == "rules":
        print(RULES)
        print("Press Enter to begin a game. Type Quit any time to quit.\n")

    keepPlaying = True
    while keepPlaying:
        game()
        playerChoice = parseInput(["", "y", "yes", "n", "no"], "Play again? Y/N: ")
        if playerChoice in ["n", "no"]:
            sys.exit()


if __name__ == '__main__':
    play()
