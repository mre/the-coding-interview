#!/usr/bin/env python3

import sys

data = map(int, sys.argv[1].split(','))
k = next(data)
seen = []
pairs = []

for n in data:
    x = k - n
    if x != n:
        if x in seen:
            pairs.append((min(x, n), max(x, n)))
        else:
            seen.append(n)

print(pairs)
