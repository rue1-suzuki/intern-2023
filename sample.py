from random import shuffle


def CALC_TOTAL(cards):
    pass


def main():
    Trump = [
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
    shuffle(Trump)

    dealers = []
    dealers.append(Trump.pop())
    dealers.append(Trump.pop())

    players = []
    players.append(Trump.pop())
    players.append(Trump.pop())

    print('ディーラーのアップカード')
    print('{} {}'.format(dealers[0]['suit'], dealers[0]['number'],))
    print('')

    while Trump.__len__() > 0:
        print('プレイヤーのカード')
        for card in players:
            print('{} {}'.format(card['suit'], card['number'],))
        print('')

        yes_or_no = input('ヒットしますか？(y/n): ')
        if yes_or_no == 'y':
            print('ヒット\n')
            players.append(Trump.pop())
        elif yes_or_no == 'n':
            print('スタンド\n')
            break
        else:
            continue

        if CALC_TOTAL(players) > 21:
            print('バースト\n')
            print('プレイヤーの敗北')
            exit()

    while Trump.__len__() > 0:
        print('ディーラーのカード')
        for card in dealers:
            print('{} {}'.format(card['suit'], card['number'],))
        print('')

        if CALC_TOTAL(dealers) >= 17:
            print('スタンド\n')
            break
        else:
            print('ヒット\n')
            dealers.append(Trump.pop())

        if CALC_TOTAL(dealers) > 21:
            print('バースト\n')
            print('ディーラーの敗北')
            exit()

    print('ディーラー: {}'.format(CALC_TOTAL(dealers)))
    print('プレイヤー: {}'.format(CALC_TOTAL(players)))
    print('')

    if CALC_TOTAL(players) > CALC_TOTAL(dealers):
        print('プレイヤーの勝利')
    elif CALC_TOTAL(dealers) > CALC_TOTAL(players):
        print('プレイヤーの敗北')
    else:
        print('引き分け')


if __name__ == '__main__':
    main()
