from random import shuffle

SUITS = ['スペード', 'クラブ', 'ダイヤ', 'ハート',]


def calc_total(cards):
    total = 0
    for card in cards:
        if card['number'] == 1:
            total += 11
        elif card['number'] > 10:
            total += 10
        else:
            total += card['number']
    for card in cards:
        if not total > 21:
            break
        if card['number'] == 1:
            total += -10
    return total


def main():
    trump_cards = [
        {'suit': 'スペード', 'number': 1, },
        {'suit': 'スペード', 'number': 2, },
        {'suit': 'スペード', 'number': 3, },
        {'suit': 'スペード', 'number': 4, },
        {'suit': 'スペード', 'number': 5, },
        {'suit': 'スペード', 'number': 6, },
        {'suit': 'スペード', 'number': 7, },
        {'suit': 'スペード', 'number': 8, },
        {'suit': 'スペード', 'number': 9, },
        {'suit': 'スペード', 'number': 10, },
        {'suit': 'スペード', 'number': 11, },
        {'suit': 'スペード', 'number': 12, },
        {'suit': 'スペード', 'number': 13, },
        {'suit': 'クラブ', 'number': 1, },
        {'suit': 'クラブ', 'number': 2, },
        {'suit': 'クラブ', 'number': 3, },
        {'suit': 'クラブ', 'number': 4, },
        {'suit': 'クラブ', 'number': 5, },
        {'suit': 'クラブ', 'number': 6, },
        {'suit': 'クラブ', 'number': 7, },
        {'suit': 'クラブ', 'number': 8, },
        {'suit': 'クラブ', 'number': 9, },
        {'suit': 'クラブ', 'number': 10, },
        {'suit': 'クラブ', 'number': 11, },
        {'suit': 'クラブ', 'number': 12, },
        {'suit': 'クラブ', 'number': 13, },
        {'suit': 'ダイヤ', 'number': 1, },
        {'suit': 'ダイヤ', 'number': 2, },
        {'suit': 'ダイヤ', 'number': 3, },
        {'suit': 'ダイヤ', 'number': 4, },
        {'suit': 'ダイヤ', 'number': 5, },
        {'suit': 'ダイヤ', 'number': 6, },
        {'suit': 'ダイヤ', 'number': 7, },
        {'suit': 'ダイヤ', 'number': 8, },
        {'suit': 'ダイヤ', 'number': 9, },
        {'suit': 'ダイヤ', 'number': 10, },
        {'suit': 'ダイヤ', 'number': 11, },
        {'suit': 'ダイヤ', 'number': 12, },
        {'suit': 'ダイヤ', 'number': 13, },
        {'suit': 'ハート', 'number': 1, },
        {'suit': 'ハート', 'number': 2, },
        {'suit': 'ハート', 'number': 3, },
        {'suit': 'ハート', 'number': 4, },
        {'suit': 'ハート', 'number': 5, },
        {'suit': 'ハート', 'number': 6, },
        {'suit': 'ハート', 'number': 7, },
        {'suit': 'ハート', 'number': 8, },
        {'suit': 'ハート', 'number': 9, },
        {'suit': 'ハート', 'number': 10, },
        {'suit': 'ハート', 'number': 11, },
        {'suit': 'ハート', 'number': 12, },
        {'suit': 'ハート', 'number': 13, },
    ]
    shuffle(trump_cards)

    dealer_cards = []
    dealer_cards.append(trump_cards.pop())
    dealer_cards.append(trump_cards.pop())

    player_cards = []
    player_cards.append(trump_cards.pop())
    player_cards.append(trump_cards.pop())

    print('ディーラーのアップカード')
    print('{} {}'.format(dealer_cards[0]['suit'], dealer_cards[0]['number'],))
    print('')

    while trump_cards.__len__() > 0:
        print('プレイヤーのカード')
        for card in player_cards:
            print('{} {}'.format(card['suit'], card['number'],))
        print('')

        yes_or_no = input('ヒットしますか？(y/n): ')
        if yes_or_no == 'y':
            print('ヒット\n')
            player_cards.append(trump_cards.pop())
        elif yes_or_no == 'n':
            print('スタンド\n')
            break
        else:
            continue

        if calc_total(player_cards) > 21:
            print('バースト\n')
            print('プレイヤーの敗北')
            exit()

    while trump_cards.__len__() > 0:
        print('ディーラーのカード')
        for card in dealer_cards:
            print('{} {}'.format(card['suit'], card['number'],))
        print('')

        if calc_total(dealer_cards) >= 17:
            print('スタンド\n')
            break
        else:
            print('ヒット\n')
            dealer_cards.append(trump_cards.pop())

        if calc_total(dealer_cards) > 21:
            print('バースト\n')
            print('ディーラーの敗北')
            exit()

    print('ディーラー: {}'.format(calc_total(dealer_cards)))
    print('プレイヤー: {}'.format(calc_total(player_cards)))
    print('')

    if calc_total(player_cards) > calc_total(dealer_cards):
        print('プレイヤーの勝利')
    elif calc_total(dealer_cards) > calc_total(player_cards):
        print('プレイヤーの敗北')
    else:
        print('引き分け')


if __name__ == '__main__':
    main()
