import sys
t = int(sys.stdin.readline())

for casen in xrange(t):
    line = sys.stdin.readline().strip()
    linea = line.split(" ")
    r = int(linea[0])
    t = int(linea[1])

    lo = 0
    hi = 10000000000
    while hi > lo + 1:
        mid = (lo + hi) / 2
        if 2*r*mid + (2*mid-1)*mid <= t:
            lo = mid
        else:
            hi = mid
    print "Case #%d: %d" % (casen+1, lo)
