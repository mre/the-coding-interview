import sys

def check(elements, player):
	allowed = [player] + ['T']
	return all(element in allowed for element in elements)

def win_row(board, row, player):
	elements = []
	for i in range(4):
		elements.append(board[row][i])
	return check(elements, player)

def win_col(board, col, player):
	elements = []
	for i in range(4):
		elements.append(board[i][col])
	return check(elements, player)

def win_diags(board, player):
	d1 = []
        d2 = []
	for i in range(4):
		d1.append(board[i][i])
		d2.append(board[i][3-i])
	return check(d1, player) or check(d2, player)

def finished(board):
    return not any(board[x][y] == '.' for x in range(4) for y in range(4))

def check_board(board):
	for player in ['X', 'O']:
		for row in range(4):
			if win_row(board, row, player):
				return player + " won"

		for col in range(4):
			if win_col(board, col, player):
				return player + " won"

		if win_diags(board, player):
			return player + " won"

	if not finished(board):
		return "Game has not completed"

	return "Draw"


numcases = int(sys.stdin.readline())
for casenum in range(1,numcases+1):
	board = []
	for i in range(5):
		board.append(sys.stdin.readline().strip())
	print "Case #" + repr(casenum) + ": " + check_board(board)
