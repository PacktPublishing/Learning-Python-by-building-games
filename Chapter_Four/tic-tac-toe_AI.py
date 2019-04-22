import random
def printBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def isWinner(board, current_player):
    return ((board[7] == current_player and board[8] == current_player and board[9] == current_player) or
    (board[4] == current_player and board[5] == current_player and board[6] == current_player) or
    (board[1] == current_player and board[2] == current_player and board[3] == current_player) or 
    (board[7] == current_player and board[4] == current_player and board[1] == current_player) or
    (board[8] == current_player and board[5] == current_player and board[2] == current_player) or
    (board[9] == current_player and board[6] == current_player and board[3] == current_player) or
    (board[7] == current_player and board[5] == current_player and board[3] == current_player) or
    (board[9] == current_player and board[5] == current_player and board[1] == current_player))

def makeMove(board, current_player, move):
    board[move] = current_player

def boardCopy(board):
    cloneBoard = []
    for pos in board:
        cloneBoard.append(pos)
    
    return cloneBoard


def isSpaceAvailable(board,move):
    return board[move] == ' '

def getRandomMove(board, moves):
    availableMoves = []
    for move in moves:
        if isSpaceAvailable(board, move):
            availableMoves.append(move)
    
    if availableMoves.__len__() != 0:
        return random.choice(availableMoves)
    else:
        return None        


def makeComputerMove(board, computerPlayer):
    if computerPlayer == 'X':
        humanPlayer = 'O'
    else:
        humanPlayer = 'X'
    #part 1 
    for pos in range(1,10):
        #pos is for position of board layout
        clone = boardCopy(board)
        if isSpaceAvailable(clone, pos):
            makeMove(clone, computerPlayer, pos)
            if isWinner(clone, computerPlayer):
               return pos


    for pos in range(1,10):
        clone = boardCopy(board)
        if isSpaceAvailable(clone, pos):
            makeMove(clone, humanPlayer, pos)
            if isWinner(clone, humanPlayer):
               return pos

    if isSpaceAvailable(board, 5):
        return 5

    move = getRandomMove(board, [1,3,7,9])
    if move != None:
        return move

    #moves for remaining places ==> [2,4,6,8]
    return getRandomMove(board, [2,4,6,8])

def makePlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceAvailable(board, int(move)):
        print('What is your next move? (choose between 1-9)')
        move = int(input())
        return move

def main():
    while True:
        board = [' '] * 10
        player, computer = 'X', 'O'
        turn = 'human'
        print("The " + turn + " will start the game")
        isGameRunning = True
        
        while isGameRunning:
            if turn == 'human':
                printBoard(board)
                move = makePlayerMove(board)
                makeMove(board, player, move)
                if isWinner(board, player):
                    printBoard(board)
                    print("You won the game!")
                    isGameRunning = False
                else:
                    turn = 'computer'
            else:
                move = makeComputerMove(board, computer)
                makeMove(board, computer, move)
                if isWinner(board, computer):
                    printBoard(board)
                    print('You loose!')
                    isGameRunning = False
                else:
                    turn = 'human'
                       
main() #calling main function
    
