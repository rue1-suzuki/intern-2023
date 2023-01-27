from random import shuffle
from typing import List

from Player import Player
from Trump import Trump


class Blackjack:
    trump: Trump
    dealer: Player
    players: List[Player]

    def __init__(self, player_of_number: int) -> None:
        self.dealer = Player(name='ディーラー', is_dealer=True, )
        self.players = [
            Player(name=f'プレイヤー{index + 1}', credit=200,)
            for index in range(player_of_number)
        ]

    def games(self) -> None:
        while self.players.__len__() > 1:
            print(f'残り {self.players.__len__()} 名')
            self.game()
            new_players = []
            for member in self.players:
                if member.is_active():
                    new_players.append(member)
                else:
                    print(f'{member.name} が 脱落')
            self.players = new_players

        if self.players.__len__() == 1:
            print(f'優勝: {self.players[0].name}')
        else:
            print('プレイヤーが全滅しました。')

    def game(self) -> None:
        self._game_init()
        self._burst_or_hit_or_stand()
        self._result()

    def _game_init(self) -> None:
        shuffle(self.players)
        self.trump = Trump()

        for member in self.players + [self.dealer]:
            member.cards = [self.trump.pick_card() for _ in range(2)]
            member.add_credit(-100)
            member.print_upcard()
            if not member.is_dealer:
                member.print_credit()
            print('')
        print('')

    def _burst_or_hit_or_stand(self) -> None:
        for member in self.players + [self.dealer]:
            print(f'{member.name} の ターン')
            while self.trump.cards.__len__() > 0:
                member.print_cards()

                if member.calc_total() > 21:
                    print('バースト\n')
                    break

                if member.is_dealer:
                    not_break_players = list(filter(
                        lambda x: not x.calc_total() > 21,
                        self.players,
                    ))
                    if not_break_players.__len__() == 0:
                        break

                if member.is_hit():
                    print('ヒット\n')
                    member.cards.append(self.trump.pick_card())
                else:
                    print('スタンド\n')
                    break

    def _result(self) -> None:
        for member in self.players + [self.dealer]:
            print(f'{member.name}: {member.calc_total()}')
        print('')

        dealer_total = self.dealer.calc_total()
        for member in self.players:
            member_total = member.calc_total()
            if member_total > 21:
                # print(f'{member.name} が バースト')
                is_win = False
            elif dealer_total > 21:
                # print(f'{self.dealer.name} が バースト')
                is_win = True
            elif member_total < dealer_total:
                is_win = False
            elif member_total > dealer_total:
                is_win = True
            else:
                is_win = None

            if is_win is None:
                print(f'{member.name}: 引き分け')
                member.add_credit(100)
            elif is_win:
                print(f'{member.name}: 勝利')
                member.add_credit(200)
            else:
                print(f'{member.name}: 敗北')
        print('')


if __name__ == '__main__':
    blackjack = Blackjack(player_of_number=3)
    blackjack.games()
