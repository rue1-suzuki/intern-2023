SUITS = ['スペード', 'クラブ', 'ダイヤ', 'ハート', ]


class Card:
    suit: int
    number: int

    def __init__(self, suit: int, number: int, ) -> None:
        self.suit = suit
        self.number = number

    def __str__(self):
        if self.number == 1:
            return '{} {}'.format(SUITS[self.suit], 'A', )
        elif self.number == 11:
            return '{} {}'.format(SUITS[self.suit], 'J', )
        elif self.number == 12:
            return '{} {}'.format(SUITS[self.suit], 'Q', )
        elif self.number == 13:
            return '{} {}'.format(SUITS[self.suit], 'K', )

        return '{} {}'.format(SUITS[self.suit], self.number, )
