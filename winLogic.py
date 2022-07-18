import board


def update_board(player):
    win = False
    # check row
    for i in board.game:
        if i.count(player) == 3:
            win = True
    # check column
    for c in range(3):
        count = 0
        for r in range(3):
            if board.game[r][c] == player:
                count += 1
        if count == 3:
            win = True
    # check diagonals
    if board.game[0][0] == player and board.game[1][1] == player and board.game[2][2] == player:
        win = True
    if board.game[2][0] == player and board.game[1][1] == player and board.game[0][2] == player:
        win = True
    return win

