from enum import Enum
import random

class Players(Enum):
    X = 'X'
    O = 'O'
    EMPTY = ' '

def initialize_board():
    return [[(row, col, Players.EMPTY) for col in range(3)] for row in range(3)]

def print_board(board):
    for row in board:
        print(' | '.join(cell[2].value for cell in row))
        if row != board[-1]:
            print('--------')

def check_win(board, player):
    for direction in [(1, 0), (0, 1), (1, 1), (1, -1)]:
        for row in range(3):
            for col in range(3):
                try:
                    if all(board[row + direction[0]*i][col + direction[1]*i][2] == player for i in range(3)):
                        return True
                except IndexError:
                    continue
    return False

def is_board_full(board):
    return all(cell[2] == Players.EMPTY for row in board for cell in row)

def get_ai_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col][2] == Players.EMPTY]
    return random.choice(empty_cells)

def play_tic_tac_toe(ai_mode=True):
    board = initialize_board()
    players = list(Players)[:2]
    current_player = random.choice(players)

    while True:
       
        print_board(board)
        

        if current_player == Players.X:
            row, col = map(int, input("Player X's turn (row column): ").split())
        else:
            if current_player == Players.O and ai_mode:
                row, col = get_ai_move(board)
            else:
                row, col = map(int, input("Player O's turn (row column): ").split())

        if board[row][col][2] == Players.EMPTY:
            board[row][col] = (row, col, current_player)

            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player.name} wins!")
                return

            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                return

            current_player = Players.X if current_player == Players.O else Players.O
        else:
            print("Cell already occupied. Please choose a different one.")
print("These are the instructions on how to play this TicTacToe game.\nYou are automatically assigned either player X or O at random.\nThe following are the coordinates for each cell: \n TopLeft=0 0 , TopMiddle= 0 1 , TopRight= 0 2 \n MiddleLeft=1 0 , MiddleMiddle= 1 1 , MiddleRight= 1 2 \n  BottomLeft=2 0 , BottomMiddle= 2 1 , BottomRight= 2 2 \n Enjoy my game \n ")
play_tic_tac_toe(ai_mode=False)
