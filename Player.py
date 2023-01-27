from typing import List

from Card import Card


class Player:
    name: str
    cards: List[Card]
    is_dealer: bool
    credit: int

    def __init__(self, name: str, is_dealer: bool = False, credit: int = 0) -> None:
        self.name = name
        self.cards = []
        self.is_dealer = is_dealer
        self.credit = credit

    def print_upcard(self) -> None:
        print(f'アップカード: {self.cards[0]}')

    def print_credit(self) -> None:
        print(f'クレジット: {self.credit}')

    def add_credit(self, added_credit: int) -> None:
        self.credit += added_credit
        if self.credit < 0:
            self.credit = 0

    def print_cards(self) -> None:
        # print(f'{self.name} の カード')
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
            yes_or_no = input(f'{self.name}: ヒットしますか？(y/n): ')
            if yes_or_no == 'y':
                return True
            elif yes_or_no == 'n':
                return False
            else:
                print('yまたはnを入力してください。\n')
                continue

    def is_active(self) -> bool:
        return self.credit > 0
