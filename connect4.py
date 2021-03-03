import numpy as np
ROW_COUNT = 6
COLUMN_COUNT= 7
def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[5][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r-1][c] == piece and board[r-2][c]==piece and board[r-3][c]==piece:
                return True
board = create_board()
print_board(board)
game_over = False
turn = 0
while not game_over:
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6) : "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,1)
        if winning_move(board,1):
            print("Player 1 Wins!!! Congrats....")
            game_over = True


    else:
        col = int(input("Player 2 make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board,row,col,2)
        if winning_move(board, 2):
            print("Player 2 Wins!!! Congrats....")
            game_over = True
            break

    print_board(board)
    turn += 1
    turn %= 2
