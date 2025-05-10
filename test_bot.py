from random import randint
from copy import deepcopy

def test_bot(p) :
    board = [[ "-" for _ in range (7)] for _ in range(6)] 

    ran_col = randint(0,6)
    for r in range(6):
        board[r][ran_col] = "X"

    other_col = randint(0,6)
    while other_col == ran_col:
        other_col = randint(0,6)
    
    for r in range(3):
        board[r][other_col] = "X"

    orginal_board = deepcopy(board)
    
    try:
        col = p(board, "X")

        if board != orginal_board:
            print("Bot editted original board")
            return False
        
        if col == ran_col:
            print("Bot chose full column")
            return False
        
        if col > 6 or col < 0:
            print("Bot return invalid column")
            return False
    except Exception as e:
        print("Bot raised an exception:", e)
        return False
    return True