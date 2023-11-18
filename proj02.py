import math
from copy import deepcopy

# make board with the range 0f 3X3
board = [['*' for x in range(3)] for y in range(3)]

# gave symbols
player = 'X'
computer = 'O'

# printing board
def printing_board(board):
    for row in board:
        print(" ".join(row))
    print()

# check win for the player
def checking_for_win(board, player):
    # for row
    for row in board:
        if row.count(player) == 3:
            return True
    # for column
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # for diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    # not any one win
    return False

# for tie
def check_tie(board):
    for row in board:
        if '*' in row:
            return False
    return True


def minimax(board, depth, is_maximizing_player):
    if checking_for_win(board, computer):
        return 10 - depth
    elif checking_for_win(board, player):
        return depth - 10
    elif check_tie(board):
        return 0
    if is_maximizing_player:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '*':
                    board_copy = deepcopy(board)
                    board_copy[row][col] = computer
                    score = minimax(board_copy, depth+1, False)
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '*':
                    board_copy = deepcopy(board)
                    board_copy[row][col] = player
                    score = minimax(board_copy, depth+1, True)
                    best_score = min(score, best_score)
        return best_score

# Get the optimal move for the computer player
def get_computer_move(board):
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '*':
                board_copy = deepcopy(board)
                board_copy[row][col] = computer
                score = minimax(board_copy, 0, False)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


# starting game loop
print("Here is your Complete Board")
while True:
    # Get player move
    printing_board(board)
    row = int(input("Enter your row for move (0-2): "))
    col = int(input("Enter your column for move (0-2): "))
    #checking for the invalid move
    if board[row][col] != '*':
        print("Invalid move. Try again.")
        continue
    board[row][col] = player
    if checking_for_win(board, player):
        printing_board(board)
        print("You have Won the Game!")
        break
    if check_tie(board):
        printing_board(board)
        print("Your Game become Tie!")
        break

    # Get computer move
    print("Computer Making the Move")
    row, col = get_computer_move(board)
    board[row][col] = computer
    if checking_for_win(board, computer):
        printing_board(board)
        print("Computer have Won the Game!")
        break
