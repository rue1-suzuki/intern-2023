SUITS = ['スペード', 'クラブ', 'ダイヤ', 'ハート', ]

PICTURE_CARDS = [
    {'number': 1, 'picture': 'A', },
    {'number': 11, 'picture': 'J', },
    {'number': 12, 'picture': 'Q', },
    {'number': 13, 'picture': 'K', },
]


class Card:
    suit: int
    number: int

    def __init__(self, suit: int, number: int, ) -> None:
        self.suit = suit
        self.number = number

    def __str__(self) -> str:
        for picture_card in PICTURE_CARDS:
            if self.number == picture_card['number']:
                picture = picture_card['picture']
                return f'{SUITS[self.suit]} {picture}'

        return f'{SUITS[self.suit]} {self.number}'
