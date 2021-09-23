import numpy
board = numpy.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
player1_symbol = 'X'
player2_symbol = 'O'


def place_symbol(symbol):
    print(numpy.matrix(board))
    while True:
        row = int(input("Input Row to place symbol (1,2,3): "))
        col = int(input("Input Column to place symbol (1,2,3): "))
        if 0 < row < 4 and 0 < col < 4 and board[row-1][col-1] == '-':
            break
        else:
            print("Invalid input. Enter again")
    board[row - 1][col - 1] = symbol


def check_rows(symbol):
    for r in range(3):
        count = 0
        for c in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won!")
            return True
    return False


def check_cols(symbol):
    for c in range(3):
        count = 0
        for r in range(3):
            if board[r][c] == symbol:
                count += 1
        if count == 3:
            print(symbol, "won!")
            return True
    return False


def check_diagonal(symbol):
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] == symbol:
        print(symbol, "won!")
        return True
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] == symbol:
        print(symbol, "won!")
        return True
    else:
        return False


def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonal(symbol)


def play():
    for turn in range(9):
        if turn % 2 == 0:
            print("It's X's turn")
            place_symbol(player1_symbol)
            if won(player1_symbol):
                break
        else:
            print("It's O's turn")
            place_symbol(player2_symbol)
            if won(player2_symbol):
                break
    if not(won(player1_symbol)) and not(won(player2_symbol)):
        print("It's a draw")


play()
