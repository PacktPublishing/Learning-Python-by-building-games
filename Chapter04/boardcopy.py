def makeMove(board, current_player, move):
    board[move] = current_player


def boardCopy(board):
    cloneBoard = []
    for pos in board:
        cloneBoard.append(pos)

    return cloneBoard
