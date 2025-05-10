def move_func(board, symbol):
    ls = ["0", '1', '2', '3', '4', '5', '6']
    ans = input("Enter Move, 0-6:")
    while ans not in ls:
        ans = input("Try again EnterMove:")
    return int(ans)