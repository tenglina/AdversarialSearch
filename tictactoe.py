"""
Tic Tac Toe Player
"""
import copy
import math

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

    x_count = 0
    o_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    poss = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                poss.add((i, j))

    return poss


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res = copy.deepcopy(board)

    try:
        if res[action[0]][action[1]] is EMPTY:
            res[action[0]][action[1]] = player(board)
            return res
    except():
        raise Exception("Invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    d1 = [0, 0, 0]
    d2 = [0, 0, 0]
    # check rows and cols
    for i in range(3):
        row = board[i]
        col = [row[i] for row in board]
        if row.count(X) == 3 or col.count(X) == 3:
            return X
        elif row.count(O) == 3 or col.count(O) == 3:
            return O
        else:
            d1[i] = board[i][i]
            d2[2 - i] = board[i][2-i]

    if d1.count(X) == 3 or d2.count(X) == 3:
        return X
    elif d1.count(O) == 3 or d2.count(O) == 3:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True

    else:
        return len(actions(board)) == 0


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
    else:
        play = player(board)
        if play == X:
            if board == initial_state():
                return 0, 0

            v = -1000
            move = (None,None)
            for action in actions(board):
                res = minim(result(board, action))
                if res > v:
                    v = res
                    move = action

            return move

        else:
            v = 10000
            move = (None, None)
            for action in actions(board):
                res = maxim(result(board, action))
                if res < v:
                    v = res
                    move = action

            return move


def minim(board):
    if terminal(board):
        return utility(board)
    else:
        v = 1000
        for action in actions(board):
            temp = result(board, action)
            v = min(v, maxim(temp))

        return v


def maxim(board):
    if terminal(board):
        return utility(board)
    else:
        v = -1000
        for action in actions(board):
            temp = result(board, action)
            v = max(v, minim(temp))
        return v
