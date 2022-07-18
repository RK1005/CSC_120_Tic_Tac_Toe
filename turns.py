import board
import winLogic

def print_board():
    for i in board.game:
        print(i)


def check_board(row, col):
    if row <= 3 and col <= 3:
        if board.game[row-1][col-1] == '-':
            return True
    else:
        return False

def place_mark(player):
    while True:
        r = int(input("Enter row number: "))
        c = int(input("Enter col number: "))
        if check_board(r, c):
            board.game[r-1][c-1] = player
            print_board()
            break
        else:
            print("Enter valid units for row and col.")

def turns(player_turn):
    if player_turn == 'X':
        print("Player one turn:")
        place_mark(player_turn)
    if player_turn == 'O':
        print("Player two turn:")
        place_mark(player_turn)
turn = 1
while True:
    if turn > 0:
        turns('X')
        turn = turn * -1
        if winLogic.update_board('X'):
            print("Player X has won!!")
            break
    else:
        turns('O')
        turn = turn * -1
        if winLogic.update_board('O'):
            print("Player O has won!!")
            break
