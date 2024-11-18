"""
Tic Tac Toe Player
"""

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
    for row in board:
        for column in row:
            if column == X:
                x_count += 1
            elif column == O:
                o_count += 1
    
    # If there are more X than O then it's O's chance else it's X's chance.
    if x_count > o_count:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty.add((i,j))
    return empty


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [row[:] for row in board]  # Create a copy of the board

    if action is None:
        return new_board
    
    # Apply the player's move to the new board
    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # If no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:  # Check if there is a winner
        return True
    
    for row in board:  # Check if the board is full (no empty spaces)
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X: return 1
    if result == O: return -1
    return 0

def minValue(board):
    if terminal(board):
        return utility(board)
    value = float('inf') 
    for action in actions(board):
        value = min(value, maxValue(result(board, action)))
    return value

def maxValue(board):
    if terminal(board):
        return utility(board)

    value = float('-inf') 
    # Checking all the outcome value of each action and setting minimum as value
    for action in actions(board):
        value = max(value, minValue(result(board, action)))
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Let's say player is X, X will want to take action with max output value. 
    We'll take the max value of all the minimum values that O's next turn can output since O will try to minimize the output value in it's turn.
    We'll keep going down and down until the game is finished.
    """
    # Ensure there are valid actions
    possible_actions = actions(board)
    if not possible_actions:
        return None  # No possible actions (game over)

    current_player = player(board)
    if current_player == X:
        # Maximizing player (X)
        best_value = float('-inf')
        best_action = None
        for action in actions(board):
            action_value = minValue(result(board, action))
            if action_value > best_value:
                best_value = action_value
                best_action = action
        return best_action

    elif current_player == O:
        # Minimizing player (O)
        best_value = float('inf')
        best_action = None
        for action in actions(board):
            action_value = maxValue(result(board, action))
            if action_value < best_value:
                best_value = action_value
                best_action = action
        return best_action

