from typing import List

from Player import Player
from Trump import Trump

MAX_PLAYERS = 3

BET_CREDIT = 100
FIRST_CREDIT = BET_CREDIT * 2
WIN_CREDIT = BET_CREDIT * 2
LOSE_CREDIT = BET_CREDIT * 0
DRAW_CREDIT = BET_CREDIT * 1


class Blackjack:
    trump: Trump
    dealer: Player
    players: List[Player]

    def __init__(self) -> None:
        while True:
            try:
                player_of_number = int(input(
                    f'プレイヤーの人数を入力してください。(1～{MAX_PLAYERS}): '
                ))
            except ValueError:
                continue

            if player_of_number < 1 or MAX_PLAYERS < player_of_number:
                print(f'1～{MAX_PLAYERS}で入力してください。')
                continue
            break
        print('')

        self.dealer = Player(
            name='ディーラー',
            is_dealer=True,
        )
        self.players = [
            Player(
                name=f'プレイヤー{index + 1}',
                credit=FIRST_CREDIT,
            )
            for index in range(player_of_number)
        ]

    def games(self) -> None:
        while self.players.__len__() > 1:
            self.game()
            new_players = []
            for member in self.players:
                if member.is_active():
                    new_players.append(member)
                else:
                    print(f'脱落: {member.name}')
            print('')
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
        self.trump = Trump()

        for member in self.players + [self.dealer]:
            print(member.name)
            member.cards = [
                self.trump.pick_card()
                for _ in range(2)
            ]
            member.print_upcard()

            if not member.is_dealer:
                member.print_credit()
                member.add_credit(-BET_CREDIT)
                print(f'↓ -{BET_CREDIT}')
                member.print_credit()

            print('')
        print('')

    def _burst_or_hit_or_stand(self) -> None:
        for member in self.players + [self.dealer]:
            print(f'{member.name} の ターン')

            # プレイヤーが全員バーストしている場合、ディーラーは何もしない
            if member.is_dealer:
                not_break_players = list(filter(
                    lambda x: not x.calc_total() > 21,
                    self.players,
                ))
                if not_break_players.__len__() == 0:
                    print('プレイヤーが全員バースト \n')
                    break

            while self.trump.cards.__len__() > 0:
                member.print_cards()

                if member.calc_total() > 21:
                    print('バースト\n')
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
                is_win = False
            elif dealer_total > 21:
                is_win = True
            elif member_total < dealer_total:
                is_win = False
            elif member_total > dealer_total:
                is_win = True
            else:
                is_win = None

            if is_win is None:
                print(f'{member.name}: 引き分け (+{DRAW_CREDIT})')
                member.add_credit(DRAW_CREDIT)
            elif is_win:
                print(f'{member.name}: 勝ち (+{WIN_CREDIT})')
                member.add_credit(WIN_CREDIT)
            else:
                print(f'{member.name}: 負け (+{LOSE_CREDIT})')
                member.add_credit(LOSE_CREDIT)
        print('')


if __name__ == '__main__':
    blackjack = Blackjack()
    if blackjack.players.__len__() > 1:
        blackjack.games()
    else:
        while True:
            blackjack.game()
            if input('次のゲームを始めますか？(y/n): ') == 'n':
                break
