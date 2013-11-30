def board(h, w):
    board = []
    for row in range(h):
        row = [row*w + col for col in range(1,w+1)]
        board.append(row)
    return board

def spiral(h, w, r, c):
    b = board(h, w)
    # up left down right
    directions = [(0,-1),(-1,0),(0,1),(1,0)]
    # step: 1 1 2 2 3 3 4 4 5 5 ...
    step = 1
    # Start positions
    x = c-1
    y = r-1
    print b[y][x]
    count = 0
    # Stop a top right corner
    while True:
        modx, mody = directions[count % 4]
        for s in step():
            x = x + modx
            y = y + mody
            if 0 <= x <= w-1 and 0 <= y <= h-1:
                print b[y][x]
            if y == 0 and x == w-1:
                # We're done
                return
        count += 1
        if count % 2 == 0:
            # Increase step at each second count
            step += 1


spiral(2,4,1,2)
