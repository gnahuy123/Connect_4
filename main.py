import bots
import bots.Play_urself
import bots.Yu_Hangs_Bot_v0
import bots.bot0
from test_bot import test_bot
import random

def is_draw(board):
    for c in range(7):
        if board[5][c] == "-":
            return False
    return True

def print_board(board):
    print("\nCurrent Board:")
    for r in reversed(range(6)):
        print(" | ".join(board[r]))
    print("   ".join(map(str, range(7))))
    print("\n")

def create_board():
    board = [[ "-" for _ in range (7)] for _ in range(6)] #0,0 is bottome left; 6,0 is bottom right; 0,5 is top left; 6,5 is top right
    return board

def change_board(board, col, symbol):
    for r in range(6):
        if board[r][col] == "-":
            board[r][col] = symbol
            return

def check_win(board):
    #check horizontal
    for r in range(3):
        for c in range(7):
            if board[r][c] != "-":
                if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c]:
                    return True
                
    #check vertical
    
    for r in range(6):
        for c in range(4):
            if board[r][c] != "-":
                if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3]:
                    return True

    #check positive diagianal

    for r in range(3):
        for c in range(4):
            if board[r][c] != "-":
                if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3]:
                    return True

    
    #check negative diaganal

    for r in range(3,6):
        for c in range(4):
            if board[r][c] != "-":
                if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3]:
                    return True
                
    return False

class Player:
    def __init__(self, symbol: str, func):
        self.symbol = symbol
        self.func = func

    def move(self, board) -> int:
        return self.func(board, self.symbol)


#p0 -> 0 p1 -> 1 draw -> 2
def game(player0, player1, print_bool):
    #test functions/player first

    board = create_board()
    player_idx = random.randint(0,1)
    if player_idx == 0:
        cur_player = player0
    else:
        cur_player = player1
    
    if print_bool: 
        print_board(board)

    while not is_draw(board):
        
        col = cur_player.move(board)
        #check bounds
        change_board(board, col, cur_player.symbol)
        idx = player_idx % 2
        if check_win(board):
            if print_bool:
                print_board(board)
            #print("Player {0} wins".format(idx))
            return idx
        if idx == 0:
            cur_player = player1
        else:
            cur_player = player0
        player_idx += 1
        if print_bool:
            print_board(board)
    return 2

def main():

    bot0 = bots.Yu_Hangs_Bot_v0.move_func #insert bot here
    bot1 = bots.bot0.move_func #insert benchmark bot here
    for _ in range(10):
        if not test_bot(bot0): 
            raise Exception("Your bot doesnt pass testcase" )
        if not test_bot(bot1):
            raise Exception("BenchMark bot doesnt pass testcase" )
    print("Bots pass test cases")

    player0 = Player("0", bot0)
    player1 = Player("1", bot1)   
    n = 10000
    ls = [0,0,0]     
    for _ in range(n):
       ls[game(player0, player1, False)] += 1

    print("Player0: {0}% ".format(100*ls[0]/n))
    print("Player1: {0}% ".format(100*ls[1]/n))
    print("Draw: {0}%".format(100*ls[2]/n))

def play_urself():
    bot0 = bots.Play_urself.move_func
    bot1 = bots.bot0.move_func #insert benchmark bot here
    for _ in range(10):
        if not test_bot(bot1):
            raise Exception("BenchMark bot does pass testcase")
        
    player0 = Player("0", bot0)
    player1 = Player("1", bot1)   

    res = game(player0, player1, True)
    if res == 0:
        print("You Win")
    elif res == 1:
        print("You Lose")
    else:
        print("Draw")

#if __name__ == "__main__":
    #main()

play_urself()
        
        
        
        

        

    
