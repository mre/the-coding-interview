def duplicate_characters(sequence):
    unique = set(sequence)
    return len(unique) != len(sequence)

def is_valid(sequence):
    """
    A string is not valid if the knight moves onto a blank square 
    and the string cannot contain more than two vowels.
    """
    if any(letter == " " for letter in sequence):
        return False
    # Check for vowels
    # Strings shorter than 3 letters are always ok, as they
    # can't contain more than two vowels
    if len(sequence) < 3:
        return True
    # Check longer sequences for number of vowels
    vowels="AEIO"
    num_vowels = len([v for v in sequence if v in vowels])
    if num_vowels > 2:
        return False
    # Check for duplicate characters.
    # The original question did not say anything about
    # repeated characters, but ignoring them would lead to infinite
    # sequences, such as AMAMAMA..., where the knight makes the same sequence
    # of moves over and over again
    if duplicate_characters(sequence):
        return False
    return True

def sequences(board, pos, seq = []):
    print pos
    x, y = pos
    #if 0 <= x <= len(board) - 1:
    if x in range(len(board)-1) and y in range(len(board[0])-1):
        letter = board[x][y]
    else:
        return
    letter = board[x][y]
    seq.append(letter)
    if not is_valid(seq):
        return
    yield seq
    # Continue with all other possible moves
    moves = [(-1,-2),(1,-2), (-1,2), (1,2),(-2,1),(-2,-1),(2,1),(2,-1)]
    for move in moves:
        dx, dy = move
        for s in sequences(board, (x+dy, y+dy), seq):
            print s
            yield s

def knight(board):
    result = []
    # We can start at any position on the board
    for x in range(len(board)-1):
        for y in range(len(board[0])-1):
            # Generate all move sequences from that position
            startpos = (x,y)
            for sequence in sequences(board, startpos):
                result.append("".join(sequence))
    return result

# Create the board
board = "ABC_E _GHIJ KLMNO PQRST UV__Y".split()

print knight(board)
