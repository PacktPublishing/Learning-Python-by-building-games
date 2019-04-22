def isWinner(board, current_player):
    return ((board[7] == current_player and board[8] == current_player and board[9] == current_player) or
    (board[4] == current_player and board[5] == current_player and board[6] == current_player) or
    (board[1] == current_player and board[2] == current_player and board[3] == current_player) or 
    (board[7] == current_player and board[4] == current_player and board[1] == current_player) or
    (board[8] == current_player and board[5] == current_player and board[2] == current_player) or
    (board[9] == current_player and board[6] == current_player and board[3] == current_player) or
    (board[7] == current_player and board[5] == current_player and board[3] == current_player) or
    (board[9] == current_player and board[5] == current_player and board[1] == current_player))
