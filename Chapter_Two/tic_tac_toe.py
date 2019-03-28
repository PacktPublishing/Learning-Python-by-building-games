game_board = ['_'] * 9

print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])

while True:
    pos = input('Pick a number from 0-8')
    pos = int(pos)
    game_board[pos] = 'X'
    print(game_board[0] + '|' + game_board[1] + '|' + game_board[2])
    print(game_board[3] + '|' + game_board[4] + '|' + game_board[5])
    print(game_board[6] + '|' + game_board[7] + '|' + game_board[8])



