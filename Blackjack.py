from random import shuffle
from typing import List

from Player import Player
from Trump import Trump


class Blackjack:
    trump: Trump
    dealer: Player
    players: List[Player]

    def __init__(self, player_of_number: int) -> None:
        self.trump = Trump()
        self.dealer = Player(name='ディーラー', is_dealer=True, )
        self.players = [
            Player(name='プレイヤー{}'.format(index + 1))
            for index in range(player_of_number)
        ]
        shuffle(self.players)

    def game(self) -> None:
        for member in self.players + [self.dealer]:
            for _ in range(2):
                member.add_card(card=self.trump.pick_card())
            member.print_upcard()

        for member in self.players + [self.dealer]:
            while self.trump.cards.__len__() > 0:
                member.print_cards()

                if member.calc_total() > 21:
                    print('{}: バースト\n'.format(member.name))
                    break

                if member.is_hit():
                    print('{}: ヒット\n'.format(member.name))
                    member.add_card(card=self.trump.pick_card())
                else:
                    print('{}: スタンド\n'.format(member.name))
                    break

        for member in self.players + [self.dealer]:
            print('{}: {}'.format(
                member.name,
                member.calc_total(),
            ))
        print('')

        dealer_total = self.dealer.calc_total()
        for player in self.players:
            player_total = player.calc_total()

            if player_total > 21:
                print('{}がバースト'.format(player.name))
                print('{} の 敗北'.format(player.name))
            elif dealer_total > 21:
                print('{}がバースト'.format(self.dealer.name))
                print('{} の 勝利'.format(player.name))
            else:
                if player_total < dealer_total:
                    print('{} の 敗北'.format(player.name))
                elif player_total > dealer_total:
                    print('{} の 勝利'.format(player.name))
                else:
                    print('引き分け')


if __name__ == '__main__':
    blackjack = Blackjack(player_of_number=3)
    blackjack.game()
