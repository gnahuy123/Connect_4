
from random import randint

#Randomly chooses slot
def move_func(board, symbol):
    ls = []
    for c in range(7):
        if board[5][c] == '-':
            ls.append(c)
    return ls[randint(0,len(ls)-1)]
