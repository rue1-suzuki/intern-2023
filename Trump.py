from random import shuffle
from typing import List

from Card import SUITS, Card


class Trump:
    cards: List[Card]

    def __init__(self) -> None:
        cards = []
        for suit_index in range(SUITS.__len__()):
            for number_index in range(13):
                card = Card(
                    suit=suit_index,
                    number=number_index + 1,
                )
                cards.append(card)
        shuffle(cards)
        self.cards = cards

    def pick_card(self) -> Card:
        return self.cards.pop()
