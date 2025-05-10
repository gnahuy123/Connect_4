from random import randint

#Greedily pick left most column
def move_func(board, symbol):
    col = 0
    while True:
        if board[5][col] != "-":
            col += 1
        else:
            return col