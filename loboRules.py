RULES = """
Lobo is a challenging solitaire game originally created by James Ernest.
Lobo uses the "Postas Deck", a 5 suited deck with cards ranked 1-10.
You are dealt four cards, as is your opponent the Wolf. Both hands of cards are
visible to you, and the top card of the deck is always face up. Your goal is to
empty the Wolf's hand. Even if you cannot defeat the Wolf, you are still trying
to leave it with the smallest number of points. You will play several rounds,
scoring after each round, and racing the Wolf to 100 points.

You have the choice of several actions.

PERFECT. You play one card from your hand to capture one card of the matching
rank from the Wolf's hand. Discard both card, and add the top card of the deck
to your hand.

SUM. You play more than one card from your hand which add up to capture exactly
one card in the Wolf's hand. Discard all cards involved, and add the top card of
the deck to your hand.

SPLIT. You play one card and capture more than one card from the Wolf's hand.
The cards you capture must add up to exactly the value of the card you play.
Discard all cards involved, and add the top card of the deck to the Wolf's hand.

OVER. You play one card to capture one smaller card from the Wolf's hand.
Discard both cards, and add cards to the Wolf's hand equal to the difference
in the card's ranks. There is no upper limit to the size of the Wolf's hand.

FOLD. If you feel you cannot improve your situation, you can stop at any time.
You might also be forced to stop if you have no moves left.

The wolf does not take actions, just you. You may continue taking actions until
you are out of options, or you decide to fold, or the Wolf runs out of cards.

If the Wolf is out of cards, you win the round! You score points equal to the
ranks of all the cards left in your hand. If the Wolf still has cards left, you
lose the round. The Wolf scores points equal to the ranks of all the card's left
in their hand. Your remaining cards are ignored. (Sometimes you should fold even
if you still have actions to keep the Wolf's score low)

The deck is shuffled and another hand is dealt.
Play continues until you or the Wolf reaches 100 points.

Lobo is a difficult game, and wins are rare. They say “The Wolf takes small
bites,” meaning that a player must often be satisfied with a minimal loss,
rather than a win. Choosing the right time to fold is one of the hardest
elements of perfect play. Fighting too long, or taking big risks without a
clear path to victory, can be costly.

The difficulty of the game can be adjusted by removing the highest rank cards.
Easy uses ranks 1-8.
Normal uses ranks 1-9.
Hard uses ranks 1-10.
"""
