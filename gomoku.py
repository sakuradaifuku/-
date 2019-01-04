the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(len(the_board)):
    print_board(the_board)
    print(turn + 'の番です。どこに打つ？')
    move = input()
    while (the_board[move] != ' '):
        print('その場所は既に入力されています。')
        move = input('他の場所を入力してください：')
    the_board[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


print_board(the_board)
print('終了です。お疲れ様でした。')
