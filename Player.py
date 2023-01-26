from typing import List

from Card import Card


class Player:
    name: str
    cards: List[Card]
    is_dealer: bool

    def __init__(self, name: str, is_dealer: bool = False, ) -> None:
        self.name = name
        self.cards = []
        self.is_dealer = is_dealer

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def print_upcard(self) -> None:
        print('{} の アップカード'.format(self.name))
        print(self.cards[0])
        print('')

    def print_cards(self) -> None:
        print('{} の カード'.format(self.name))
        for card in self.cards:
            print(card)
        print('')

    def calc_total(self) -> int:
        total = 0
        for card in self.cards:
            if card.number == 1:
                total += 11
            elif card.number > 10:
                total += 10
            else:
                total += card.number
        for card in self.cards:
            if not total > 21:
                break
            if card.number == 1:
                total += -10
        return total

    def is_hit(self) -> bool:
        if self.is_dealer:
            return self.calc_total() < 17

        while True:
            yes_or_no = input('{}: ヒットしますか？(y/n): '.format(self.name))
            if yes_or_no == 'y':
                return True
            elif yes_or_no == 'n':
                return False
            else:
                print('yまたはnを入力してください。\n')
                continue
