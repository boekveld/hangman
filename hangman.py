#! /usr/bin/env python3

# 独学プログラマー チャレンジ問題10.hangman
# 2019/01/16更新
# 2019/01/05初出

# ハングマンを自分でプログラミングする

import random
def hangman(word):
    listedword = list(word)
    board = ['_'] * len(word)
    tmplist = []
    wrong = 0 # 間違いは7つまでOK

    print('ハングマンを始めます。')
    print(''.join(board))
    print('{}文字の単語です。'.format(str(len(word))))

    while wrong < 8:
        print()
        char = input('文字を当ててね。  ')
        try:
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.index(char)
        except:
            print('入力がおかしいです。')
            continue
        char_upper = char.upper()
        char_lower = char.lower()

        if char_lower in listedword:
            while char_lower in listedword:
                i = listedword.index(char_lower)
                board[i] = char_lower
                listedword[i] = '$'
            if '_' not in board:
                break
        else:
            wrong += 1
        print(''.join(board))
        print('間違い: {}/8'.format(wrong))

    if wrong < 8:
        print('\nあなたの勝ちです。')
        print('単語は{}、間違いは{}回でした。'.format(word, wrong))
    else:
        print('\nあなたの負けです。')
        print('単語は{}でした。'.format(word))
#    print('word: {}, char: {}, wrong: {}, listedword: {}, board: {}'.format(word, char_upper, wrong, listedword, board))

# 答の単語を選ぶ
wordlist = [
    'beer',
    'wine',
    'mead',
    'king',
    'vodka',
    'queen',
    'watch',
    'joint',
    'point',
    'chain',
    'bread',
    'river',
    'green',
    'salad',
    'yield',
    'field',
    'peach',
    'beech',
    'beach',
    'brain',
    'grace',
    'melon',
    'lemon',
    'stain',
    'chaos',
    'crane',
    'stone',
    'clock',
    'notch',
    'score',
    'storm',
    'tiger',
    'train'
    'stream'
    'crystal'
    'trigger',
    ] 
hangman(wordlist[random.randrange(0, len(wordlist) - 1)])
