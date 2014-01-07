import sys
rl = sys.stdin.readline

def sum(n):
    return (n * (n + 1)) / 2

def can_draw(r, t, rings):
    t -= (2 * r + 1) * rings
    t -= sum(rings - 1) * 4
    return t >= 0

T = int(rl())
for cc in xrange(T):
    r, t = map(int, rl().split())

    can, cannot = 1, t + 1

    while can + 1 < cannot:
        middle = (can + cannot) / 2
        if can_draw(r, t, middle):
            can = middle
        else:
            cannot = middle
    print 'Case #%d: %d' % (cc + 1, can)
