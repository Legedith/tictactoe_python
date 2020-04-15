"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    nx =  len([1 for i in board for j in i if j==X])
    no =  len([1 for i in board for j in i if j==O])
    return O if no<nx else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i,row in enumerate(board):
        for j,col in enumerate( row):
            if col == EMPTY:
                action.add((i,j))
    return action
    



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    brd = copy.deepcopy(board)
    if brd[action[0]][action[1]] != EMPTY:
        raise NameError('NonValidMove')
    else:
        brd[action[0]][action[1]] = player(board)
        return brd

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check who made the last move
    mv = X if player(board)== O else O
    # print(board)
    # print(mv)
    # for itterate over each row and columnb and see if three are in a row:
    #rows
    for i in range(3):
        for j in range(3):
            if board[i][j] != mv:
                break
            if j == 2:
                return mv
    #cols
    for i in range(3):
        for j in range(3):
            if board[j][i] != mv:
                break
            if j == 2:
                return mv
     #diagonal
    for i in range(3):
        if board[i][i] != mv:
            # print(i)
            break
        if i == 2:
            return mv
    #Anti-diagonal
    for i in range(3):
        if board[i][2-i] != mv:
            break
        if i == 2:
            return mv

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        # print("here")
        if any([True for i in board for j in i if j==None]):
            return False
    # print(winner(board))
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    p = player(board)
    moves = tree(board)
    
    if p == X:
        return [i for  i in moves.keys() if moves[i] == max(moves.values())][0]
    else:
        return [i for  i in moves.keys() if moves[i] == min(moves.values())][0]
    
def tree(board):
    # print('.',end=", ")
    p = player(board)
    mv = actions(board)
    d = {}
    for i in mv:
        d[i]=0
    for i in mv:
        # print(i)
        res = result(board, i)
        # print(res)
        if(terminal(res)):
            d[i] = utility(res)
        else:
            dtemp = tree(result(board,i))
            # print(dtemp,i," 444",d)
            if p == O:
                d[i]= max(dtemp.values())
                # print("O's turn : ",d)
            else:
                d[i]= min(dtemp.values())
                # print("X's turn : ",d)
    # print(i,d,p)
    return d