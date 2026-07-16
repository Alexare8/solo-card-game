from deck import Deck
from card import Card
from lobo_rules import RULES, QUICK_RULES
import sys


def parse_input(options: list[str], message: str = "") -> str:
    while True:
        raw_input_string = input(message)
        input_string = raw_input_string.lower()
        if input_string in ["quit", "q", "exit"]:
            sys.exit()
        if input_string in ["full rules", "fullrules"]:
            print(RULES)
        elif input_string in options:
            return input_string


def select_card(card_list: list[Card]) -> Card:
    selection = parse_input([str(card.rank) for card in card_list], "Enter a card rank: ")
    selection = int(selection)
    for card in card_list:
        if card.rank == selection:
            return card


def select_multiple_cards(source_list: list[Card]) -> list[Card]:
    selection = []
    card_list = [card for card in source_list]
    first_card = select_card(card_list)
    selection.append(first_card)
    card_list.remove(first_card)
    print(f"Selected Total: {sum([card.rank for card in selection])}. Cards: {", ".join([str(card) for card in card_list])}.")
    second_card = select_card(card_list)
    selection.append(second_card)
    card_list.remove(second_card)
    select_again = True
    while select_again:
        if len(card_list) == 0:
            break
        print(f"Selected Total: {sum([card.rank for card in selection])}. Cards: {", ".join([str(card) for card in card_list])}.")
        card_input = parse_input([str(card.rank) for card in card_list] + [""], "Press Enter to stop or enter a card rank: ")
        another_card = None
        if card_input == "":
            select_again = False
        else:
            for card in card_list:
                if card.rank == int(card_input):
                    another_card = card
            selection.append(another_card)
            card_list.remove(another_card)
    return selection


def game_round(difficulty) -> tuple[bool, int]:
    rank_offset = 0
    if difficulty == "easy":
        rank_offset = 2
    if difficulty == "normal":
        rank_offset = 1

    RANKS = [(num, str(num)) for num in range(1, 11 - rank_offset)]
    SUITS = [(5, "★"), (4,"♠"), (3,"♦"), (2,"♣"), (1,"♥")]
    deck = Deck(RANKS, SUITS)
    deck.shuffle()
    player_hand = [deck.draw() for _ in range(4)]
    wolf_hand = [deck.draw() for _ in range(4)]

    continue_round = True
    while continue_round:
        try:
            print(f"Wolf hand: {", ".join([str(card) for card in wolf_hand])}")
            print(f"Your hand: {", ".join([str(card) for card in player_hand])}")
            print(f"Top card: {deck.peek_top()}")
            match parse_input(["perfect", "sum", "split", "over", "fold", "rules"], "PERFECT, SUM, SPLIT, OVER, FOLD, or RULES? "):

                case "perfect":
                    print("Select a card from your hand: ")
                    played_card = select_card(player_hand)
                    targeted_card = None
                    card_match = False
                    for wolf_card in wolf_hand:
                        if played_card.rank == wolf_card.rank:
                            card_match = True
                            targeted_card = wolf_card
                            wolf_hand.remove(wolf_card)
                    if card_match:
                        player_hand.remove(played_card)
                    else:
                        raise ValueError("No PERFECT matching card in Wolf's hand.")

                    print(f"{played_card} removes {targeted_card}.")
                    new_card = deck.draw()
                    player_hand.append(new_card)
                    print(f"You get {new_card}.")

                case "sum":
                    print("Select cards from your hand: ")
                    played_cards = select_multiple_cards(player_hand)
                    targeted_card = None
                    total = sum([card.rank for card in played_cards])
                    card_match = False
                    for wolf_card in wolf_hand:
                        if total == wolf_card.rank:
                            card_match = True
                            targeted_card = wolf_card
                            wolf_hand.remove(wolf_card)
                            break
                    if card_match:
                        for card in played_cards:
                            player_hand.remove(card)
                    else:
                        raise ValueError(f"No card in Wolf's hand matching SUM {total}.")

                    print(f"{", ".join([str(card) for card in played_cards])} removes {targeted_card}.")
                    new_card = deck.draw()
                    player_hand.append(new_card)
                    print(f"You get {new_card}.")

                case "split":
                    print("Select cards from the Wolf's hand: ")
                    played_card = None
                    targeted_cards = select_multiple_cards(wolf_hand)
                    total = sum([card.rank for card in targeted_cards])
                    card_match = False
                    for player_card in player_hand:
                        if total == player_card.rank:
                            card_match = True
                            played_card = player_card
                            player_hand.remove(player_card)
                            break
                    if card_match:
                        for card in targeted_cards:
                            wolf_hand.remove(card)
                    else:
                        raise ValueError(f"No card in your hand matching SPLIT {total}.")

                    print(f"{played_card} removes {", ".join([str(card) for card in targeted_cards])}.")
                    new_card = deck.draw()
                    wolf_hand.append(new_card)
                    print(f"The Wolf gets {new_card}.")

                case "over":
                    print("Select a card from your hand: ")
                    played_card = select_card(player_hand)
                    print("Select a card from the Wolf's hand: ")
                    targeted_card = select_card(wolf_hand)
                    if not played_card.greater_than(targeted_card):
                        raise ValueError(f"{played_card} is not greater than {targeted_card}.")
                    difference = played_card.rank - targeted_card.rank
                    player_hand.remove(played_card)
                    wolf_hand.remove(targeted_card)

                    print(f"{played_card} removes {targeted_card}.")
                    for _ in range(difference):
                        new_card = deck.draw()
                        print(f"The Wolf gets {new_card}.")
                        wolf_hand.append(new_card)

                case "fold":
                    continue_round = False

                case "rules":
                    print(QUICK_RULES)

            print("")
            if len(player_hand) == 0 or len(wolf_hand) == 0:
                continue_round = False

        except Exception as e:
            print(f"Error: {e}")

    if len(wolf_hand) == 0:
        score = sum([card.rank for card in player_hand])
        print(f"You win the round! You score {score} points.")
        return (True, score)
    else:
        score = sum([card.rank for card in wolf_hand])
        print(f"You lose the round. The Wolf scores {score} points.")
        return (False, score)


def game(difficulty: str) -> None:
    player_score = 0
    wolf_score = 0
    while (player_score < 100 and wolf_score < 100):
        result = game_round(difficulty)
        if result[0]:
            player_score += result[1]
        else:
            wolf_score += result[1]
        print(f"You: {player_score} Wolf: {wolf_score}\n")
    if wolf_score > 100:
        print("You lose.")
    else:
        print("You win!")


def play() -> None:
    print("Welcome to Lobo!")
    start_input = parse_input(["rules", ""], "Press Enter to begin a game. Type RULES for an explanation. Type QUIT to quit.\n")
    if start_input == "rules":
        print(RULES)
        parse_input([""], ("Press Enter to begin a game. Type QUIT at any time to quit. "))

    keep_playing = True
    while keep_playing:
        difficulty = parse_input(["easy", "normal", "hard"], "Easy, Normal, or Hard? ")
        print("")
        game(difficulty)
        player_choice = parse_input(["", "y", "yes", "n", "no"], "Play again? Y/N: ")
        if player_choice in ["n", "no"]:
            sys.exit()


if __name__ == '__main__':
    play()
