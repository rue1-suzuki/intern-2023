from random import shuffle
from typing import List

from Card import SUITS, Card


class Trump:
    cards: List[Card]

    def __init__(self) -> None:
        cards = []
        for suit in range(SUITS.__len__()):
            for number in range(1, 1 + 13):
                card = Card(
                    suit=suit,
                    number=number,
                )
                cards.append(card)
        shuffle(cards)
        self.cards = cards

    def pick_card(self) -> Card:
        return self.cards.pop()
