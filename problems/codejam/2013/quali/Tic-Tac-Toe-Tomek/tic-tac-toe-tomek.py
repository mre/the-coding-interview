import sys, time

def get_data():
    numcases = int(sys.stdin.readline())
    for case in range(1,numcases+1):
        data = []
        while True:
            line = sys.stdin.readline().strip()
            if line:
                data.append(line)
            else:
                break
        yield (case, data)

def main():
    for case, data in get_data():
        print solve(data)

"""
Quick and dirty
"""
def solve(board):
    # Check rows
    count_x, count_o, count_t = 0,0,0
    for x in range(4):
        # Check xth row
        for y in range(4):
            if board[x][y] == 'X':
                count_x += 1
            if board[x][y] == 'O':
                count_o += 1
            if board[x][y] == 'T':
                count_t += 1
        if count_x == 4:
            return "X won"
        if count_o == 4:
            return "O won"
        if count_x == 3 and count_t == 1:
            return "X won"
        if count_o == 3 and count_t == 1:
            return "O won"
        count_x, count_o, count_t = 0,0,0
    # Check columns
    count_x, count_o, count_t = 0,0,0
    for y in range(4):
        for x in range(4):
            if board[x][y] == 'X':
                count_x += 1
            if board[x][y] == 'O':
                count_o += 1
            if board[x][y] == 'T':
                count_t += 1
        if count_x == 4:
            return "X won"
        if count_o == 4:
            return "O won"
        if count_x == 3 and count_t == 1:
            return "X won"
        if count_o == 3 and count_t == 1:
            return "O won"
        count_x, count_o, count_t = 0,0,0
    # Check diags
    count_x, count_o, count_t = 0,0,0
    for x in range(4):
        if board[x][x] == 'X':
            count_x += 1
        if board[x][x] == 'O':
            count_o += 1
        if board[x][x] == 'T':
            count_t += 1
    if count_x == 4:
        return "X won"
    if count_o == 4:
        return "O won"
    if count_x == 3 and count_t == 1:
        return "X won"
    if count_o == 3 and count_t == 1:
        return "O won"
    count_x, count_o, count_t = 0,0,0
    for x in range(1,5):
        if board[x-1][4-x] == 'X':
            count_x += 1
        if board[x-1][4-x] == 'O':
            count_o += 1
        if board[x-1][4-x] == 'T':
            count_t += 1
    if count_x == 4:
        return "X won"
    if count_o == 4:
        return "O won"
    if count_x == 3 and count_t == 1:
        return "X won"
    if count_o == 3 and count_t == 1:
        return "O won"
    # Check empty cells
    for x in range(4):
        for y in range(4):
            if board[x][y] == ".":
                return "Game has not completed"
    return "Draw"






"""
Bug ridden
"""
def solve2(board):
    players = ['X', 'O']
    wildcard = 'T'
    empty = '.'
    board_size = len(board)
    for player in players:
        # Check rows
        for x in range(board_size):
            if all(s == player or s == wildcard for s in board[x]): return player + " won"
            # Check columns
            if all(s == player or s == wildcard for y in range(board_size) for s in board[y][x]): return player + " won"
        # Check diagonals
        if all(s == player or s == wildcard for s in board[x][x] for x in range(board_size)): return player + " won"
        if all(s == player or s == wildcard for s in board[x][4-x] for x in range(board_size)): return player + " won"

    if any(s == empty for x in range(board_size) for y in range(board_size) for s in board[x][y]): 
        return "Game has not completed"
    else:
        return "Draw"

if __name__ == "__main__":
    main()
